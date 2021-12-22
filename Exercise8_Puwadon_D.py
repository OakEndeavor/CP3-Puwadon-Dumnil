usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput=="Endeavor" and passwordInput=="oaken narakkk":
    print("Login Success")
    print("ยินดีต้อนรับสู่ PD Book Shop ครับ")
    print("สนใจหนังสือแนวไหนเชิญเลือกได้เลยครับ")
    print("---------------------------------------------------------")
    print("1.บริหารธุรกิจและการเงิน")
    print("2.จิตวิทยา")
    print("3.Cryptocurrency")
    print("4.พัฒนาตนเอง")
    print("---------------------------------------------------------")
    userselected = int(input("แนวหนังสือที่ต้องการ :"))
    print("---------------------------------------------------------")
    if userselected == 1:
        print("หนังสือบริธุรกิจและการเงิน")
        print("1.พ่อรวยสอนลูก 300 บาท")
        print("2.เปลี่ยนเลนเป็นเศรษฐี 500 บาท")
        print("3.คิดแบบยิว ทำแบบญี่ปุ่น 250 บาท")
        print("4.ผู้ประกอบการคนต่อไปต้องเป็นคุณ 300 บาท")
        print("---------------------------------------------------------")
        userselectedbook = int(input("หนังสือที่ท่านเลือกซื้อ :"))
        if userselectedbook == 1:
           N1 = int(input("จำนวนเล่มที่คุณต้องการ :"))
           price1 = 300*N1
           print("ราคารวมทั้งหมด = ",price1,"บาท")
        elif userselectedbook == 2:
             N2 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price2 = 500*N2
             print("ราคารวมทั้งหมด = ",price2,"บาท")
        elif userselectedbook == 3:
             N3 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price3 = 250*N3
             print("ราคารวมทั้งหมด = ",price3)
        elif userselectedbook == 4:
             N4 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price4 =300*N4
             print("ราคารวมทั้งหมด : ",price4,"บาท")
    elif userselected == 2:
         print("หนังสือจิตวิทยา")
         print("1.ขุนเขาเกาสมอง 200 บาท")
         print("2.พฤติกรรมและจิตวิทยาการลงทุน 250 บาท")
         print("3.Trading in the zone 500 บาท")
         print("---------------------------------------------------------")
         userselectedbook2 = int(input("หนังสือที่ท่านต้องการเลือก :"))
         if userselectedbook2 == 1:
            N5 = int(input("จำนวนเล่มที่คุณต้องการ :"))
            price5 = 200*N5
            print("ราคารวมทั้งหมด :",price5,"บาท")
         elif userselectedbook2 == 2:
            N6 = int(input("จำนวนเล่มที่คุณต้องการ :"))
            price6 = 250*N6
            print("ราคารวมทั้งหมด :",price6,"บาท")
         elif userselectedbook2 == 3:
             N7 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price7 = 500*N7
             print("ราคารวมทั้งหมด :",price7,"บาท")
    elif userselected == 3:
         print("หนังสือเกี่ยวกับ Cryptocurrency")
         print("1.Bitcoin&Blockchain 101")
         print("2.Bitcoin Standard")
         print("3.Digital Asset Investment 101")
         print("---------------------------------------------------------")
         userselectedbook3 = int(input("หนังสือที่ท่านต้องการเลือก :"))
         if userselectedbook3 == 1:
             N7 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price7 = 300 * N7
             print("ราคารวมทั้งหมด :", price7, "บาท")
         elif userselectedbook3 == 2:
             N8 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price8 = 500 * N8
             print("ราคารวมทั้งหมด :", price8, "บาท")
         elif userselectedbook3 == 3:
             N9 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price9 = 500 * N9
             print("ราคารวมทั้งหมด :", price9, "บาท")
    elif userselected == 4:
         print("หนังสือพัฒนาตัวเอง")
         print("1.กินกบตัวนั้นซะ 125 บาท")
         print("2.Atom Habbit 400 บาท")
         print("3.คิดใหญ่ คิดไม่เล็ก 250 บาท")
         print("---------------------------------------------------------")
         userselectedbook4 = int(input("หนังสือที่ท่านต้องการเลือก :"))
         if userselectedbook4 == 1:
             N10 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price10 = 125 * N10
             print("ราคารวมทั้งหมด :", price10, "บาท")
         elif userselectedbook4 == 2:
             N11 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price11 = 400 * N11
             print("ราคารวมทั้งหมด :", price11, "บาท")
         elif userselectedbook4 == 3:
             N12 = int(input("จำนวนเล่มที่คุณต้องการ :"))
             price12 = 250 * N12
             print("ราคารวมทั้งหมด :", price12, "บาท")
    print("---------------------------------------------------------")
    print("------------------------THANK YOU------------------------")
else:
    print("Login Failed!! (T_T)")
    print("Try again.")




