import os
import ast
import math
import csv
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from radon.raw import analyze
from collections import Counter

# Define the folder path
base_dir = os.getcwd()
code_folder = os.path.join(base_dir, 'code_solutions')  #folder  that has  code   solutions in .py
csv_file_path = os.path.join(base_dir, 'code_metrics_GPT4.csv')  # output file  

def get_file_number(filename):
    return int(filename.split('_')[1].split('.')[0])

def compute_halstead_metrics(file_content):
    # Initialize counters for operators and operands
    operators = set()
    operands = set()
    operator_count = Counter()
    operand_count = Counter()

    # Parse the code into an AST
    tree = ast.parse(file_content)

    # Walk through the AST to find operators and operands
    for node in ast.walk(tree):
        # Operators: such as arithmetic, assignment, comparisons
        if isinstance(node, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod,
                             ast.Pow, ast.LShift, ast.RShift, ast.BitOr,
                             ast.BitXor, ast.BitAnd, ast.FloorDiv,
                             ast.And, ast.Or, ast.Not, ast.Invert, ast.UAdd,
                             ast.USub, ast.Eq, ast.NotEq, ast.Lt, ast.LtE,
                             ast.Gt, ast.GtE, ast.Is, ast.IsNot, ast.In,
                             ast.NotIn, ast.AugAssign, ast.Assign)):
            operators.add(type(node).__name__)
            operator_count[type(node).__name__] += 1

        # Operands: variable and literal names
        elif isinstance(node, ast.Name):
            operand_name = node.id  # For variable names
            operands.add(operand_name)
            operand_count[operand_name] += 1
        elif isinstance(node, ast.Constant):
            operand_value = node.value  # For literal values
            operands.add(str(operand_value))
            operand_count[str(operand_value)] += 1

    # Calculate Halstead Metrics
    h1 = len(operators)  # Number of distinct operators
    h2 = len(operands)   # Number of distinct operands
    N1 = sum(operator_count.values())  # Total number of operators
    N2 = sum(operand_count.values())   # Total number of operands

    # Halstead formulas
    vocabulary = h1 + h2
    length = N1 + N2
    volume = length * (math.log2(vocabulary) if vocabulary > 0 else 0)
    difficulty = (h1 / 2) * (N2 / h2) if h2 > 0 else 0
    effort = volume * difficulty
    time = effort / 18
    bugs = volume / 3000

    return {
        'h1': h1, 'h2': h2, 'N1': N1, 'N2': N2, 'vocabulary': vocabulary,
        'length': length, 'volume': volume, 'difficulty': difficulty,
        'effort': effort, 'time': time, 'bugs': bugs
    }

def count_parameters(file_content):
    tree = ast.parse(file_content)
    parameters = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            parameters += len(node.args.args)
    return parameters

def calculate_coupling(file_content):
    afferent_coupling = 0  # Stub: Find all incoming dependencies
    efferent_coupling = file_content.count('import ')
    return afferent_coupling, efferent_coupling

# Prepare CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = [
        'Filename', 'Cyclomatic Complexity', 
        'h1', 'h2', 'N1', 'N2', 'vocabulary', 'length', 'volume', 'difficulty', 'effort', 'time', 'bugs',
        'Maintainability Index', 'Source Lines of Code (SLOC)', 'Comments Ratio',
        'Number of Parameters', 'Afferent Coupling', 'Efferent Coupling', 'Instability', 'Syntax Errors'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Get all Python files and sort them
    python_files = [f for f in os.listdir(code_folder) if f.endswith('.py')]
    python_files.sort(key=get_file_number)

    # Loop through all sorted Python files in the folder
    for filename in python_files:
        file_path = os.path.join(code_folder, filename)
        print(f"Generating metrics for file: {filename}")

        # Initialize syntax errors count
        syntax_errors = 0
        metrics = {
            'Filename': filename,
            'Cyclomatic Complexity': 'Error',
            'h1': 'Error', 'h2': 'Error', 'N1': 'Error', 'N2': 'Error', 
            'vocabulary': 'Error', 'length': 'Error', 'volume': 'Error',
            'difficulty': 'Error', 'effort': 'Error', 'time': 'Error', 'bugs': 'Error',
            'Maintainability Index': 'Error',
            'Source Lines of Code (SLOC)': 'Error',
            'Comments Ratio': 'Error',
            'Number of Parameters': 'Error',
            'Afferent Coupling': 'Error',
            'Efferent Coupling': 'Error',
            'Instability': 'Error',
            'Syntax Errors': syntax_errors
        }

        try:
            # Read the file content
            with open(file_path, 'r') as file:
                file_content = file.read()

            # Calculate metrics
            complexity_data = cc_visit(file_content)
            cyclomatic_complexity = sum(block.complexity for block in complexity_data)
            halstead_metrics = compute_halstead_metrics(file_content)
            maintainability_index = mi_visit(file_content, multi=False)
            raw_analysis = analyze(file_content)
            loc = raw_analysis.loc
            sloc = raw_analysis.sloc
            comments = raw_analysis.comments
            comments_ratio = comments / loc if loc else 0
            num_parameters = count_parameters(file_content)
            afferent_coupling, efferent_coupling = calculate_coupling(file_content)
            instability = efferent_coupling / (afferent_coupling + efferent_coupling) if (afferent_coupling + efferent_coupling) != 0 else 0

            # Update metrics dictionary with actual values
            metrics.update({
                'Cyclomatic Complexity': cyclomatic_complexity,
                'h1': halstead_metrics['h1'], 'h2': halstead_metrics['h2'], 'N1': halstead_metrics['N1'], 
                'N2': halstead_metrics['N2'], 'vocabulary': halstead_metrics['vocabulary'], 
                'length': halstead_metrics['length'], 'volume': halstead_metrics['volume'], 
                'difficulty': halstead_metrics['difficulty'], 'effort': halstead_metrics['effort'], 
                'time': halstead_metrics['time'], 'bugs': halstead_metrics['bugs'],
                'Maintainability Index': maintainability_index,
                'Source Lines of Code (SLOC)': sloc,
                'Comments Ratio': comments_ratio,
                'Number of Parameters': num_parameters,
                'Afferent Coupling': afferent_coupling,
                'Efferent Coupling': efferent_coupling,
                'Instability': instability
            })

        except SyntaxError as e:
            syntax_errors += 1
            print(f"Syntax error in file {filename}: {e}")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")
            syntax_errors += 1

        # Update the syntax errors in the metrics dictionary
        metrics['Syntax Errors'] = syntax_errors

        # Write the metrics to the CSV file
        writer.writerow(metrics)

print(f"Metrics have been saved to {csv_file_path}.")
