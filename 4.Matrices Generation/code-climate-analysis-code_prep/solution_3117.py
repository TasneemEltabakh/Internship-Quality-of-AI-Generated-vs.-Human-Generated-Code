
t_sec=int(input("Enter the total Second:"))
hour=(int)(t_sec/3600)
t_sec=(int)(t_sec%3600)
mint=(int)(t_sec/60)
sec=(int)(t_sec%60)
print("Hours=",hour,"\nMinutes=",mint,"\nSecond=",sec)