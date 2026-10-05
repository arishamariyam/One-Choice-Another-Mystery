print("Welcome to One Choice, Another Mystery!")
print("Your story begins here...")
print("You wake up in a mysterious room. ")
print("there are three doors in front of you. ")
print("which door will you choose?")

choice = input("Choose a door (1 , 2 , or 3): ")

print("You chose door number", choice)

if choice == "1":
    print("You enter a dark room...")
    print("You hear someone whispering your name.")
    print("A voice says: You were not supposed to come here...")
    print("Do you want to explore the room?")
    print("1. Yes")
    print("2. No")

    action = input("Your choice: ")
    print("You entered:", action)

    if action == "1":
        print("You notice a strange shadow...")
        print("The shadow slowly moves toward you.")
        print("You see a key on the floor.")

        key = input("Do you want to take the key? (yes/no): ")

        if key == "yes":
          print("You picked up the mysterious key.")
          door = input("A locked door is ahead.Use the key? (yes/no): ")

          if door == "yes":
              print("The door slowly opens...")
              print("You discover a secret room!")
              print("You find an old diary on the table.")
              print("The diary has a strange message...")
              print("The diary says: One of these doors leads to the truth.")
              print("You hear a noise behind you.")
              print("1. Turn around")
              turn = input("Your choice: ")

              if turn == "1":
                  print("You turn around slowly...")
                  print("A shadow is standing behind you!")
                  print("The shadow whispers your name...")
                  print("Suddenly, the lights go out!")
                  print("You hear footsteps approaching...")
                  print("1. Hide under the table")
                  print("2. Run towars the door")

                  next_choice = input("What will you do? ")

                  if next_choice == "1":
                      print("You hide under the table.")
                      print("You hear footsteps entering the room...")
                      print("Someone stops right beside the table.")
                      print("You see a pair of shoes under the table...")
                      print("But there is no one standing there.")
                      print("You notice a small note on the floor.")
                      print("The note says: DON'T LOOK BEHIND YOU.")
                      look = input("Do you look behind you? (yes/no):")

                      if look == "yes":
                          print("You slowly turn around...")
                          print("The room is completely empty.")
                          print("Then your phone lights up by itslef.")
                          print("A mesaage appears: YOU MADE THE WRONG CHOICE")
                          print("The screen suddenly goes black.")
                          print("When you open your eyes, you are back in the mysterious room.")
                          print("But this time, only two doors are left.")
                      elif look == "no":
                          print("You stay complelety still.")
                          print("The footsteps suddenly stop.")
                          print("You wait for a few seconds...")
                          print("Then you hear a whisper: You should have looked.")
                          print("You slowly turn around.")
                          print("There is nobody there.")
                          print("But your name is written on the wall.")
                          print("THE END.")
                      else:
                          print("Inavlid choice!")
                      
                
                  elif next_choice == "2":
                      print("You run towars the door.")
                      print("You escape the room, but the shadow is still following you...")
                  else:
                     print("Invalid choice!")
               
          else:
              print("You decide not to open the door.")
        else:
           print("You left the key behind.")
    
    elif action == "2":
         print("You try to move, but the door is locked.")
    else:
         print("Invalid choices!")

elif choice =="2":
    print("You enter an abandoned library.")
    print("A mysterious book opens by itself.")
    print("You notice a name written on the first page.")
    print("It is your name.")
    print("A question appears: DO you want to read the next page? (yes/no)")
    read = input("Your choice: ")

    if read == "yes":
        print("You turn the page...")
        print("The book says: I knew you would come.")
        print("A photograph falls out of the book.")
        print("You look at it... and realize the person in the photograph is you.")
        photo = input("Do you keep the photograph? (yes/no): ")

        if photo == "yes":
            print("You keep the photograph.")
            print("The lights in the library suddenly turn on.")
            print("You look around the library...")
            print("Every book has the same name written on it.")
            print("Your name.")
            print("Suddenly, every book closes at the same time.")
            print("The photograph in your hand becomes completely blank.")
            print("A final message appears on the table:")
            print("YOU WERE NEVER IN THE LIBRARY.")
            print("THE END.")
        elif photo == "no":
            print("You leave the photograph on the table.")
            print("The photograph disappears.")
            print("You walk away from the table.")
            print("But when you look back, the photograph is there again.")
            print("This time, someone else is standing beside you in the photograph.")
            print("THE END.")
        else:
            print("Invalid choice!")
    
    elif read == "no":
        print("You close the book.")
        print("But the pages start turning by themselves.")
        print("The pages stop on a blank page.")
        print("Then a single word appears: RUN.")
    else:
        print("Invalid choice!")

elif choice =="3":
    print("You enter a room full of mirrors...")
    print("One mirror shows someone standing behind you.")
    print("You look into the mirror again.")
    print("The person in the mirror is not copying your movements.")
    print("It slowly raises its hand.")
    mirror = input("Do you touch the mirror? (yes/no): ")

    if mirror == "yes":
        print("You touch the mirror...")
        print("The glass feels warm.")
        print("A crack slowly appears across the mirror.")
        print("Behind the glass, you see a room that looks exactly like yours.")
        print("You notice someone standing inside the room.")
        print("The person looks exactly like you.")
        mirror_choice = input("Do you enter the room? (yes/no):")

        if mirror_choice == "yes":
            print("You step through the mirror...")
            print("The room suddenly goes completely silent.")
            print("You look around, but the other version of you is gone.")
            print("The mirror suddenly turns completely black.")
            print("A message appears on the glass:")
            print("YOU CHOSE TO ENTER.")
            print("THE END.")
        elif mirror_choice == "no":
            print("You step away from the mirror...")
            print("But your reflection steps closer.")
            print("You step back from the mirror.")
            print("The reflection keeps walking toward you.")
            print("Then it smiles.")
            print("THE END.")
        else:
            print("Invalid choice!")
    elif mirror == "no":
        print("You step away from the mirror.")
        print("Your reflection keeps staring at you.")
    else:
        print("Invalid choice!")

else:
    print("Invalid choice! Try again.")