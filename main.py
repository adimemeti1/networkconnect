def Sign_Up_Connect_Network():
    Host_Name_or_IP=input('Write your Host Name')
    if len(Host_Name_or_IP < 5):
        print('You need more than 9 characters')
    else:
        Pasword=int(input('Write your Pasword'))
        if len(Pasword < 8):
            print('You need more than 8 characters')
        else:
            Port=int(input('Write your Port number'))
            if len(Port>2):
                print('You need just two numbers')
            else:
                Connect=int(input('Do you want to connect'))
                while Connect == 'jo':
                    break
                else:
                    Host_Name_or_IP2=int(input('Write your Host Name or Ip'))
                    if Host_Name_or_IP2 != Host_Name_or_IP:
                        print('Incorrect')
                    else:
                        print('Correct')
                        Pasword2=int(input('Write your pasword'))
                        if Pasword2 != Pasword:
                            print('Incorrect')
                        else:
                            print('Correct')
                            Port2=int(input('Write your Port numbers'))
                            if Port2 != Port:
                                print('Incorrect')
                            else:
                                print('Correct \n now you are in youre network')
Sign_Up_Connect_Network()
