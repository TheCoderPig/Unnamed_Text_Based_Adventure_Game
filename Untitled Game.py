import random
import time
pl="Y"

thisisavariablethatwillneverbechanged=1
while thisisavariablethatwillneverbechanged>-1:
        #WARNING: THIS SOURCE CODE IS VERY MESSY. IF YOU CAN MAKE OPTIMISATIONS, PLEASE LET THE CREATOR KNOW.
        inventory=["Pillow", "Nutristick", "Nutristick", "Nutristick", "Blue Time Crystal", "Orange Time Crystal"]
        weapons=["Sword", "Bow and Arrow", "Axe", "Gun", "Hammer", "Radiobanana", "Banana", "Pillow", "Ultra Hammer", "Sword of Meer"]
        food=["Magic Meal", "Banana", "Nutristick", "Random Fruit", "Radiobanana", "Golden Banana", "Orange Time Crystal", "Blue Time Crystal"]
        equipment=["Ring of Banana", "Ring of Turns"]
        eq="Pillow" #your equipped weapon
        onhand=[None] #equipment, such as rings and stuff that can give special abilities.
        eneq=None #opponent's equipped weapon, decided later based on a random dice roll
        hp=100  #health
        enhp=100 #enemy health
        hng=160 #hunger
        d=0 #distance
        t=0 #number of turns you've survived
        mo=500 #Money
        ditch=0 #Are you stuck in a ditch?
        spt=random.randint(1,6) #decides spawn point based on random dice roll
        spt=1
        dim="over"
        def mret():
                import save.py
                inventory=save.inventory
                eq=save.eq
                onhand=save.onhand
                hp=save.hp
                hng=save.hng
                d=save.d
                t=save.t
                mo=save.mo
                ditch=save.ditch
                spt=save.spt
                dim=save.dim
        def msave():
                with open("save.py", "w") as s:
                    s.write("inventory="+str(inventory)+"\n")
                    s.write("eq="+'\''+eq+"\'\n")
                    s.write("onhand = "+str(onhand)+"\n")
                    s.write("hp="+str(hp)+"\n")
                    s.write("hng="+str(hng)+"\n")
                    s.write("d="+str(d)+"\n")
                    s.write("t="+str(t)+"\n")
                    s.write("mo="+str(mo)+"\n")
                    s.write("ditch="+str(ditch)+"\n")
                    s.write("spt="+str(spt)+"\n")
                    s.write("dim="+'\''+dim+"\'\n")

                    
        def genericadd(mo):
                var=random.randint(6,15)
                while var>0:
                        dice2=random.randint(1,26)
                        if (dice2==1 or dice2==10):
                                print("You got a Nutristick!")
                                inventory.append("Nutristick")
                                time.sleep(1)
                        elif (dice2==2 or dice2==11 or dice2==14):
                                inventory.append("Magic Meal")
                                print("You got a Magic Meal!")
                                time.sleep(1)
                        elif (dice2==3 or dice2==16):
                                inventory.append("Golden Banana")
                                print("You got a Golden Banana!")
                                time.sleep(3)
                                print("\nThe glow of this strange banana makes your instinct tell you that you must keep this, for it may prove to be a big help one day.\n")
                                time.sleep(1)
                        elif (dice2==4 or dice2==19):
                              inventory.append("Radiobanana")
                              print("You got a Radiobanana!")
                              time.sleep(1)
                        elif (dice2==6 or dice2==18 or dice2==5):
                                inventory.append("Gun")
                                print("You got a Gun!")
                                time.sleep(1)
                        elif (dice2==7 or dice2==20):
                                inventory.append("Hammer")
                                print("You got a Hammer!")
                                time.sleep(1)
                        elif (dice2==8 or dice2==12):
                                inventory.append("Banana")
                                print("You got a Banana!")
                                time.sleep(1)
                        elif (dice2==22 or dice2==21 or dice2==15):
                                inventory.append("Escape Rope")
                                print("You got an escape rope!")
                                time.sleep(1)
                        elif (dice2==9 or dice2==26 or dice2==23):
                                dice3=random.randint(500, 2000)
                                print("You got", dice3, "coins!")
                                mo=mo
                                mo=mo+dice3
                                time.sleep(1)
                        elif (dice2==24 or dice2==13 or dice2==26):
                                print("You got 2 orange time crystals!")
                                inventory.append("Orange Time Crystal")
                                inventory.append("Orange Time Crystal")
                        var=var-1
                inventory.append("Map")
                print("You got a map!")
                               

        print("\nPLEASE GIVE VALID RESPONSES ONLY, FAILING TO DO SO MAY EITHER SEND THE GAME INTO WHAT THE CREATOR CALLS A 'DEAD STATE', WHERE NOTHING WORKS AND YOU ARE FORCED TO RESET THE GAME AND LOSE ALL OF YOUR PROGRESS, OR STRAIGHT UP CRASH THE INTERPRETER.")
        print("\nThe responses in question are the capital letters in the square brackets. I do recommend keeping your caps lock on for this game, unless you are typing the name of an item you want to do something with.")
        print("\nFrom here onwards, the game starts. I hope you enjoy :D")
                

        if (spt==1):
                
                print("\nYou spawn in a lush forest full of life.")
                time.sleep(1)
                while hp>=0 or "Golden Banana" in inventory:
                    hng=hng-10
                    enhp=random.randint(100, 400)
                    if (hp<=0 and "Golden Banana" in inventory):
                            print("Your golden banana saved you!")
                            inventory.remove("Golden Banana")
                            hng=hng+100
                            hp=hp+100
                    if (hng<=30 and hng>10):
                        print("\nYou're beginning to feel a little hungry... Maybe you should eat something?")
                    if (hng<=10 and hng>0): print("You really need to eat something now.")
                    if (hng<0):
                        hng=0
                        hp=hp-10
                        print("\nYou're starving!")
                        print("\n-10 hp!")
                    if (hp<=0 and "Golden Banana" not in inventory):
                        break
                    t=t+1
                    resp=input("\nWhat will you do? (Walk [W]||Check Inventory [I]||Forage [F]||Climb a tree [C]): ")
                    
                    if (resp=='W' or resp=='w'):
                        resp2=input("North [N]||South [S]")
                        time.sleep(2)
                        dice=random.randint(-3,9)
                        if (resp2=='N' or 'n'):
                            d=d+100
                        elif (resp2=='S' or 's'):
                            d=d-100
                        if (dice==1 or dice==2 or dice==4 or dice==0):
                            print("\nYou found an abandoned box!")
                            resp2=input("Open It [O]||Leave It [L]")
                            if (resp2=='O'):
                                dice2=random.randint(1,29)
                                if (dice2==1 or dice2==11 or dice2==15):
                                    print("You got a Nutristick!")
                                    inventory.append("Nutristick")
                                elif (dice2==2 or dice2==12 or dice2==16):
                                    inventory.append("Magic Meal")
                                    print("You got a Magic Meal!")
                                elif (dice2==3):
                                    inventory.append("Sword")
                                    print("You got a Sword!")
                                elif (dice2==4):
                                    inventory.append("Bow and Arrow")
                                    print("You got a Bow!")
                                elif (dice2==5):
                                    inventory.append("Axe")
                                    print("You got an Axe!")
                                elif (dice2==6):
                                    inventory.append("Gun")
                                    print("You got a Gun!")
                                elif (dice2==7):
                                    inventory.append("Hammer")
                                    print("You got a Hammer!")
                                elif (dice2==8 or dice2==13 or dice2==17 or dice2==18):
                                    inventory.append("Banana")
                                    print("You got a Banana!")
                                    print("You don't remember the source, but you've heard that any sensible person should keep a banana on them at all times.")
                                    print("Perhaps these things are very useful and can help you when you're in a pinch? You'll probably find out eventually.")
                                elif (dice2==9):
                                    inventory.append("Pickaxe")
                                    print("You got a Useless Item!")
                                    print("It's good for nothing!")
                                elif (dice2==10 or dice2==14 or dice2==19 or dice2==20):
                                    inventory.append("Random Fruit")
                                    print("You got a Random Fruit!")
                                elif (dice2==21):
                                    print("A bottle inside the box breaks and spills its gaseous contents everywhere.")
                                    print("Wait, the contents are gaseous!?")
                                    hp=0
                                elif (dice2==22 or dice2==23 or dice2==24 or dice2==25):
                                    dice3=random.randint(50, 200)
                                    print("You got", dice3, "coins!")
                                    mo=mo+dice3
                                elif (dice2==26 or dice2==27 or dice2==28 or dice2==29):
                                        dice3=random.randint(4, 8)
                                        print("You got", dice3, "time crystals!")
                                        while dice3>0:
                                                inventory.append("Time Crystal")
                                                dice3-=1
                                else:
                                    print("The box was empty.")
                            elif (resp2=='L'):
                                pass
                        elif (dice==5 or dice==9):
                            print("\nYou found a trapdoor on the ground.")
                            resp2=input("Open it and get inside [O]||Ignore it [L]")
                            if (resp2=='O'):
                                dice2=random.randint(1,10)
                                if (dice2==1 or dice2==6 or dice2==8):
                                    print("\nYou have no idea why this trapdoor is sitting here, because for some odd reason you can just pick it up. But why would you, it's useless.")
                                    
                                elif (dice2==3 or dice2==5):
                                    d=random.randint(-10000, 10000)
                                    d=d%100
                                    d=d*100
                                    print("\nLooks like you've been teleported to a completely different part of this forest.")
                                elif (dice2==2 or dice2==4 or dice2==7):
                                    print("\nYou find yourself inside a shop.")
                                    resp3=None
                                    print("\nYou have", mo, "coins.")
                                    print("\nNutristick: 50 coins")
                                    print("Magic Meal: 150 coins")
                                    print("Banana: 50 coins")
                                    print("Random Fruit: 5 coins")
                                    print("\nSword: 400 coins")
                                    print("Bow and Arrow: 450 coins")
                                    print("Axe: 750 coins")
                                    print("Pillow: 200 coins")
                                    print("Escape Rope: 200 coins")
                                    

                                    print("\nExit: Leave the shop")
                                    while resp3!="Exit" and resp3!="exit":
                                        resp3=input("\nWhat will you buy? [CASE SENSITIVE] :")
                                        if (resp3=='Nutristick' and mo>=50):
                                            mo=mo-50
                                            inventory.append("Nutristick")
                                            print("\nBought a Nutristick!")
                                        elif (resp3=='Magic Meal' and mo>=150):
                                            mo=mo-150
                                            inventory.append("Magic Meal")
                                            print("\nBought a Magic Meal!")
                                        elif (resp3=='Banana' and mo>=50):
                                            mo=mo-50
                                            inventory.append("Banana")
                                            print("\nBought a Banana!")
                                        elif (resp3=='Random Fruit' and mo>=5):
                                            mo=mo-5
                                            inventory.append("Random Fruit")
                                            print("\nBought a Random Fruit!")
                                            time.sleep(3)
                                            print("\nWhy? Just why did you waste your money on that?")
                                            time.sleep(2)
                                            print("\nDo you not realise that there are easier and cheaper methods to get those stupid things?")
                                            time.sleep(2)
                                            print("\nOr am I blissfully unaware of your actual motive behind doing that?")
                                            time.sleep(2)
                                            print("\nWhatever.")
                                        elif (resp3=='Sword' and mo>=400):
                                            mo=mo-400
                                            inventory.append("Sword")
                                            print("\nBought a Sword!")
                                        elif (resp3=='Bow and Arrow' and mo>=450):
                                            mo=mo-450
                                            inventory.append("Bow and Arrow")
                                            print("\nBought a Bow and Arrow!")
                                        elif (resp3=='Axe' and mo>=750):
                                            mo=mo-750
                                            inventory.append("Axe")
                                            print("\nBought an Axe!")
                                        elif (resp3=='Pillow' and mo>=200):
                                            mo=mo-200
                                            inventory.append("Pillow")
                                            print("\nBought a Pillow!")
                                        elif (resp3=='Escape Rope' and mo>=200):
                                            mo=mo-200
                                            inventory.append("Escape Rope")
                                            print("\nBought an Escape Rope!")
                                            
                                        elif (resp3=='Exit' or resp3=='exit'):
                                            break
                                        else:
                                            print("\nEither you don't have enough money, or whatever you want isn't a thing.")
                                    print("You leave the shop.")
                                            
                                                
                                        
                                    
                                    
                                    
                                elif (dice2==9 or dice2==10):
                                    print("\nYou fall into a deep ditch.")
                                    print("\n-50 HP from fall damage!")
                                    hp-=50
                                    ditch=1
                                    if (hp<=0 and "Golden Banana" not in inventory):
                                        break
                                    elif (hp<=0 and "Golden Banana" in inventory):
                                        print("Your golden banana allowed you to survive.")
                                        hp=50
                                        inventory.remove("Golden Banana")
                                        
                                    while (ditch==1):
                                            if (hng<=30 and hng>10):
                                                print("\nYou're beginning to feel a little hungry... Maybe you should eat something?")
                                            if (hng<=10 and hng>0):
                                                print("You really need to eat something now.")
                                            if (hng<0):
                                                hng=0
                                                hp=hp-10
                                                print("\nYou're starving!")
                                                print("\n-10 hp!")
                                            resp3=input("What will you do? ||Use an escape rope [E]||Sit and wait [W]||Check Inventory [I] : ")
                                            if (resp3=='E' or resp3=='e'):
                                                    if 'Escape Rope' in inventory:
                                                            print("You managed to pull yourself out of the ditch. Unfortunately, your successful escape has resulted in your escape rope breaking.")
                                                            inventory.remove("Escape Rope")
                                                            ditch=0
                                                    else:
                                                            print("You don't have an escape rope!")
                                            elif (resp3=='W' or resp3=='w'):
                                                    w=random.randint(2, 28)
                                                    print("You wait for", w, "hours.")
                                                    x=random.randint(2,5)
                                                    if x==3:
                                                            print("Someone came and helped you get out.")
                                                            ditch=0
                                                    else:
                                                            print("Your wait was for nothing.")
                                                            hng=hng-w
                                            elif (resp3=='I' or resp3=='i'):
                                                    print("\n", inventory)
                                                    resp2=None
                                                    while resp2!='E':
                                                        resp2=input("\nWhat do you want to do? (Eat Something [I]||Change a weapon [W]||Discard an Item [D]||Exit [E]")
                                                        if (resp2=='I'):
                                                                resp3=None
                                                                while resp3 not in inventory or resp3 not in food:
                                                                    resp3=input("\nWhat do you want to use? (Type 'Nothing' if you don't want to use anything.)")
                                    
                                                                    if (resp3 in inventory and resp3 not in food): print("\nThat's not a food item!")
                                                                    elif (resp3 not in inventory and resp3 in food): print("\nYou don't have that!")
                                                                    elif (resp3 not in inventory and resp3 not in food): print("\nWhat is that?"); break
                                                                    elif (resp3 in inventory and resp3 in food):
                                                                        if (resp3=='Magic Meal'):
                                                                            temp=random.randint(70,100)
                                                                            hp=hp+temp
                                                                            hng=hng+90
                                                                            inventory.remove(resp3)
                                                                        if (resp3=='Nutristick'):
                                                                            temp=random.randint(40,70)
                                                                            hp=hp+temp
                                                                            hng=hng+60
                                                                            inventory.remove(resp3)
                                                                        if (resp3=='Banana'):
                                                                            temp=random.randint(30,50)
                                                                            hp=hp+temp
                                                                            hng=hng+60
                                                                            inventory.remove(resp3)
                                                                        if (resp3=='Random Fruit'):
                                                                            temp=random.randint(10,20)
                                                                            hp=hp+temp
                                                                            hng=hng+10
                                                                            inventory.remove(resp3)
                                                                        print("\nAte the ", resp3)
                                                                        print("\nRestored hp by", temp)
                                                                        print("\nHP is now", hp)
                                                                    elif (resp3=='Nothing'):
                                                                        break
                                                                    else:
                                                                        print("???")
                                                                    if (resp3=='Banana' and resp3 not in inventory): eq=None
                                        
                                    
                                   
                                        
                                                                if (resp3=='Banana' and resp3 not in inventory): eq=None
                                                    if (resp2=='W'):
                                                        resp3=None
                                                        while resp3 not in inventory or resp3 not in weapons:
                                                            print(inventory)
                                                            resp3=input("\nWhat do you want to equip?")
                                                            if (resp3 in inventory and resp3 in weapons):
                                                                eq=resp3
                                                                print("\nEquipped the ", eq)
                                                            elif (resp3 in inventory and resp3 not in weapons): print("\nThat's not a valid weapon!")
                                                            elif (resp3 not in inventory and resp3 in weapons): print("\nYou don't have that!")

                                                    if (resp2=='D'):
                                                        resp3=None
                                                        while resp3 not in inventory:
                                                            print(inventory)
                                                            resp3=input("\nWhat do you want to discard?")
                                                            if (resp3 in inventory):
                                                                inventory.pop(resp3)
                                                                print("\nDiscarded the ", resp3)
                                                                break
                                                            elif (resp3 not in inventory): print("\nYou don't have that!")
                                                    
                                                    
                                            
                                    
                        elif (dice==6 or dice==7):
                            print("\nSomeone wants to fight you!")
                            dice2=random.randint(1, 7)
                            if (dice2==1): eneq="Sword"
                            if (dice2==2): eneq="Bow and Arrow"
                            if (dice2==3): eneq="Axe"
                            if (dice2==4): eneq="Gun"
                            if (dice2==5): eneq="Hammer"
                            if (dice2==6): eneq="Banana"
                            if (dice2==7): eneq="Pillow"
                            print("The opponent has a", eneq)
                            print("You have a", eq)
                            if (eneq==eq=='Pillow'): print("Looks like it's gonna be a violent pillow fight!")
                            while enhp>0 and hp>0:
                                resp2=input("\nWhat will you do? ||Fight [F]||Eat Something [E]||Use an Item [I]||Change weapon [W]||Flee [R] : ")
                                if (resp2=='R'):
                                    dice3=random.randint(1,2)
                                    if (dice3==1 or dice3==3):
                                        print("\nYou successfully flee from the scene.")
                                        break
                                    elif (dice3==2):
                                        print("\nYou were unable to get away.")
                                if (resp2=='W'):
                                    resp3=None
                                    while resp3 not in inventory or resp3 not in weapons:
                                        print(inventory)
                                        resp3=input("\nWhat do you want to equip?")
                                        if (resp3 in inventory and resp3 in weapons):
                                            eq=resp3
                                            print("\nEquipped the ", eq)
                                        elif (resp3 in inventory and resp3 not in weapons): print("\nThat's not a valid weapon!")
                                        elif (resp3 not in inventory and resp3 in weapons): print("\nYou don't have that!")
                                if (resp2=='I'):    
                                    resp3=None
                                    while resp3 not in inventory or resp3 not in food:
                                        print(inventory)
                                        resp3=input("\nWhat do you want to use?")
                                        if (resp3 in inventory and resp3 not in food): print("\nThat's not a valid item!")
                                        if (resp3 not in inventory and resp3 in food): print("\nYou don't have that!")
                                        if (resp3 in inventory and resp3 in food):
                                            if (resp3=='Magic Meal'):
                                                temp=random.randint(70,100)
                                                hp=hp+temp
                                                hng=hng+90
                                            if (resp3=='Nutristick'):
                                                temp=random.randint(40,70)
                                                hp=hp+temp
                                                hng=hng+60
                                            if (resp3=='Banana'):
                                                temp=random.randint(30,50)
                                                hp=hp+temp
                                                hng=hng+60
                                            if (resp3=='Random Fruit'):
                                                temp=random.randint(10,20)
                                                hp=hp+temp
                                                hng=hng+10
                                            print("\nAte the ", resp3)
                                            print("\nRestored hp by", temp)
                                            print("\nHP is now", hp)
                                            inventory.remove(resp3)
                                            if (resp3=='Banana' and resp3 not in inventory): eq=None
                                            break
                                    if (resp3=='Banana' and resp3 not in inventory): eq=None
                                if (resp2=='F'):
                                    if (eq=='Sword'):
                                        print("\nYou slash the opponent with your sword.")
                                        dmg=random.randint(10, 35)
                                        enhp=enhp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("Opponent has ", enhp, "hp left!")
                                    if (eq=='Bow and Arrow'):
                                        dice3=random.randint(1,6)
                                        dt=dice3
                                        dmg=0
                                        while dice3>0:
                                            temp=random.randint(5, 15)
                                            dmg=dmg+temp
                                            dice3=dice3-1
                                        print("\nYou shoot", dt, "arrow(s) at your opponent.")
                                        print("\n-", dmg, "hp!")
                                        enhp=enhp-dmg
                                        print("Opponent has ", enhp, "hp left!")
                                    
                                    if (eq=='Axe'):
                                        print("\nYou swing your axe at the opponent.")
                                        dmg=random.randint(20, 50)
                                        enhp=enhp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("Opponent has ", enhp, "hp left!")
                                    if (eq=='Gun'):
                                        dice3=random.randint(1,4)
                                        dt=dice3
                                        dmg=0
                                        while dice3>0:
                                            temp=random.randint(15, 40)
                                            dmg=dmg+temp
                                            dice3=dice3-1
                                        print("\nYou fire", dt, "bullet(s) at your opponent.")
                                        print("\n-", dmg, "hp!")
                                        enhp=enhp-dmg
                                        print("Opponent has ", enhp, "hp left!")
                                    if (eq=='Banana'):
                                        print("\nYou fling your banana at the opponent.")
                                        dmg=random.randint(0, 40)
                                        enhp=enhp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("\n-5 hp from mild radiation poisoning!")
                                        enhp=enhp-5
                                        print("Opponent has ", enhp, "hp left!")
                                    if (eq=='Pillow'):
                                        print("\nYou smother the opponent with your pillow.")
                                        dmg=random.randint(-10, 20)
                                        enhp=enhp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("Opponent has ", enhp, "hp left!")
                                    if (eq=='Hammer'):
                                        print("\nYou bonk the opponent with your hammer.")
                                        dmg=random.randint(40, 100)
                                        enhp=enhp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("Opponent has ", enhp, "hp left!")
                                    if (eq=='Sword of Meer'):
                                        print("\nYou attack the opponent with your new sword.")
                                        dice3=random.randint(2,6)
                                        dt=dice3
                                        dmg=0
                                        while dice3>0:
                                            temp=random.randint(50, 200)
                                            dmg=dmg+temp
                                            dice3=dice3-1
                                        print("\nSlashed", dt, "times.")
                                        print("\n-", dmg, "hp!")
                                        enhp=enhp-dmg
                                        print("\nOpponent has", enhp, "left!")
                                    if (eq=='Ultra Hammer'):
                                        print("\nYou get a good smack at the opponent with your new hammer.")
                                        dmg=random.randint(100, 1200)
                                        enhp=enhp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("Opponent has ", enhp, "hp left!")
                                    if (eq=='Radiobanana'):
                                        
                                        dice3=random.randint(4,12)
                                        dt=dice3
                                        dmg=0
                                        while dice3>0:
                                            temp=random.randint(30, 150)
                                            dmg=dmg+temp
                                            dice3=dice3-1
                                        print("\nHit", dt, "times.")
                                        print("\n-", dmg, "hp!")
                                        print("\n- 50 hp from severe radiation poisoning!")
                                        enhp=enhp-(dmg+50)
                                        print("\nOpponent has", enhp, "left!")
                                        
                                    if (eq==None):
                                        print("\nYou don't have a weapon equipped! Why did you eat that banana???")
                                if (enhp<=0):
                                    print("\nYou defeated the opponent!")
                                    break
                                if (eneq=='Sword'):
                                        print("\nThe opponent takes a slash at you with their sword.")
                                        dmg=random.randint(10, 35)
                                        hp=hp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("You have ", hp, "hp left!")
                                if (eneq=='Bow and Arrow'):
                                        dice3=random.randint(1,6)
                                        dt=dice3
                                        dmg=0
                                        while dice3>0:
                                            temp=random.randint(5, 15)
                                            dmg=dmg+temp
                                            dice3=dice3-1
                                        print("\nYour opponent shoots", dt, "arrow(s) at you.")
                                        print("\n-", dmg, "hp!")
                                        hp=hp-dmg
                                        print("You have ", hp, "hp left!")
                                if (eneq=='Axe'):
                                        print("\nThe opponent swings their axe at you.")
                                        dmg=random.randint(20, 50)
                                        hp=hp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("You have ", hp, "hp left!")
                                if (eneq=='Gun'):
                                        dice3=random.randint(1,4)
                                        dt=dice3
                                        dmg=0
                                        while dice3>0:
                                            temp=random.randint(15, 40)
                                            dmg=dmg+temp
                                            dice3=dice3-1
                                        print("\nYour opponent fires", dt, "bullet(s) at you.")
                                        print("\n-", dmg, "hp!")
                                        hp=hp-dmg
                                        print("You have ", hp, "hp left!")
                                if (eneq=='Banana'):
                                        print("\nThe opponent flings their banana at you.")
                                        dmg=random.randint(0, 40)
                                        hp=hp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("\n-5 hp from mild radiation poisoning!")
                                        hp=hp-5
                                        print("You have ", hp, "hp left!")
                                if (eneq=='Pillow'):
                                        print("\nThe opponent smothers you with their pillow.")
                                        dmg=random.randint(-10, 20)
                                        hp=hp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("You have ", hp, "hp left!")
                                if (eneq=='Hammer'):
                                        print("\nThe opponent bonks you with their hammer.")
                                        dmg=random.randint(35, 90)
                                        hp=hp-dmg
                                        print("\n-",dmg,"hp!")
                                        print("You have ", hp, "hp left!")
                                if (hp<=0 and "Golden Banana" in inventory):
                                        print("Your golden banana gave you a second chance!")
                                        inventory.remove("Golden Banana")
                                        hp=100
                                        hng=hng+100
                        elif dice==8:
                                dice2=random.randint(1,3)
                                if dice2==2:
                                        print("\nYou found a chest!")
                                        resp2=input("Open It [O]||Leave It [L]")
                                        if (resp2=='O' or resp2=='o'):
                                                genericadd(mo)
                                        elif (resp2=='L' or resp2=='l'):
                                                print("Why? You're missing a great opportunity to get some good stuff.")
                                                time.sleep(2)
                                                print("I guess you can't make all decisions on your own. I'll open the chest for you.")
                                                time.sleep(1)
                                                genericadd(mo)
                    if (resp=='I'):
                        print("\n", inventory)
                        resp2=None
                        while resp2!='E':
                            resp2=None    
                            resp2=input("\nWhat do you want to do? (Eat something [S]||Use an item [U]||Change a weapon [W]||Discard an Item [D]||Exit [E]")
                            if (resp2=='S' or resp2=='s'):
                                        resp3=None
                                        while resp3 not in inventory or resp3 not in food:
                                            resp3=input("\nWhat do you want to eat? (Type 'Nothing' if you don't want to eat anything.)")
                                            if (resp3 in inventory and resp3 not in food): print("\nThat's not a food item!")
                                            elif (resp3 not in inventory and resp3 in food): print("\nYou don't have that!")
                                            elif (resp3 not in inventory and resp3 not in food): print("\nWhat is that?"); break
                                            elif (resp3 in inventory and resp3 in food):
                                                if (resp3=='Magic Meal'):
                                                    temp=random.randint(70,100)
                                                    hp=hp+temp
                                                    hng=hng+90
                                                    inventory.remove(resp3)

                                                if (resp3=='Nutristick'):
                                                    temp=random.randint(40,70)
                                                    hp=hp+temp
                                                    hng=hng+60
                                                    inventory.remove(resp3)

                                                if (resp3=='Banana'):
                                                    temp=random.randint(30,50)
                                                    hp=hp+temp
                                                    hng=hng+60
                                                    inventory.remove(resp3)
                                                if (resp3=='Random Fruit'):
                                                    temp=random.randint(10,20)
                                                    hp=hp+temp
                                                    hng=hng+10
                                                    inventory.remove(resp3)
                                                if (resp3=='Orange Time Crystal'):
                                                    temp=random.randint(100, 150)
                                                    hng+=150
                                                    hp+=temp
                                                    inventory.remove(resp3)
                                                    msave()
                                                if (resp3=='Blue Time Crystal'):
                                                    mret()
                                                    if resp3 in inventory:
                                                            inventory.remove(resp3)
                                                print("\nAte the ", resp3)
                                                print("\nRestored hp by", temp)
                                                print("\nHP is now", hp)
                                            elif (resp3=='Nothing'):
                                                break
                                            else:
                                                print("???")
                                            if (resp3=='Banana' and resp3 not in inventory): eq=None
                                        if (resp3=='Banana' and resp3 not in inventory): eq=None
                            elif (resp2=='U' or resp2=='u'):
                                    print(inventory)
                                    resp3=input("What do you want to use? : ")
                                    if resp3=='Map':
                                            inventory.remove("Map")
                                            w=random.randint(1, 3)
                                            print("\nYou follow the map to the red X.")
                                            time.sleep(3)
                                            if w==2:
                                                    print("\nThe map leads to nothing.")
                                            elif w==1:
                                                    if "Sword of Meer" in inventory:
                                                            y=random.randint(1, 3)
                                                            if y==1:
                                                                    print("\nThe map led you to the legendary Sword of Meer!")
                                                                    time.sleep(4)
                                                                    print("\nYou closely inspect the sword, feeling a little suspicious. You then proceed to realise that this is simply a fake sword that was butchered then glued to a hard rock and that you just got duped. I do not know if this happened due to bad luck or some sort of issue with something.")
                                                                    print("Whatever the case, You now realise that you've wasted quite a bit of your time reading all of this text and are wondering why you didn't just skip this mini-wall of text :)")
                                                                    print("\nAnyways, back to the game.")
                                                            elif y==2:
                                                                    print("The map led you to the legendary-")
                                                                    time.sleep(2)
                                                                    print("empty rock?")
                                                                    time.sleep(5)
                                                                    print("Whatever.")
                                                            elif y==3:
                                                                    print("\nThe map led you to the legendary-")
                                                                    time.sleep(3)
                                                                    print("You proceed to realise that you were just here and you have already taken what this map has led you to.")
                                                    else:
                                                            print("\nThe map led you to the legendary Sword of Meer!")
                                                            time.sleep(3)
                                                            print("\nYou spend far more energy than necessary to take the sword, because for some reason some idiot decided to lodge the sword in the middle of a hard rock. I bet that idiot was the guy who designed the sword. It could be anyone though, we cannot tell for sure.")
                                                            inventory.append("Sword of Meer")
                                                            hng=hng-20
                                            elif w==3:
                                                    if "Ultra Hammer" in inventory:
                                                            y=random.randint(1, 3)
                                                            if y==1:
                                                                    print("\nThe map led you to the Ultra Hammer!")
                                                                    time.sleep(4)
                                                                    print("\nYou closely inspect the weapon, feeling a little suspicious. You then proceed to realise that this is simply a fake hammer made of cardboard, with barely any effort put into it to make it look remotely close to the real thing. At least they glued it to a rock so that anyone who tried to take it would end up destroying it.")
                                                                    print("If you actually read this mini-wall of text, all I can say is, Thank you for being patient enough to read this. (Under the assumption that you're actually reading it.)")
                                                                    print("\nAnyways, back to the game.")
                                                            elif y==2:
                                                                    print("The map led you to-")
                                                                    time.sleep(2)
                                                                    print("a rock?")
                                                                    time.sleep(5)
                                                                    print("It does seem to be a pretty good weapon, being quite dense and large. You could bonk someone to death with it, but you can't be bothered because you've already got something far better.")
                                                            elif y==3:
                                                                    print("\nThe map led you to the-")
                                                                    time.sleep(3)
                                                                    print("You decide to not waste your time because you remembered that you were just here.")
                                                    else:
                                                         print("\nThe map led you to the Ultra Hammer!")
                                                         time.sleep(3)
                                                         print("\nYou spend far more energy than necessary to lift the sword, because of how heavy it is.")
                                                         time.sleep(1)
                                                         print("\nOF COURSE IT'S THAT HEAVY, IT'S MEANT TO BONK PEOPLE TO DEATH.")
                                                         inventory.append("Ultra Hammer")
                                                         hng=hng-20   
                            elif (resp2=='W' or resp2=='w'):
                                resp3=None
                                while resp3 not in inventory or resp3 not in weapons:
                                    print(inventory)
                                    resp3=input("\nWhat do you want to equip? : ")
                                    if (resp3 in inventory and resp3 in weapons):
                                        eq=resp3
                                        print("\nEquipped the ", eq)
                                    elif (resp3 in inventory and resp3 not in weapons): print("\nThat's not a valid weapon!")
                                    elif (resp3 not in inventory and resp3 in weapons): print("\nYou don't have that!")

                            elif (resp2=='D' or resp2=='d'):
                                resp3=None
                                while resp3 not in inventory:
                                    print(inventory)
                                    resp3=input("\nWhat do you want to discard?")
                                    if (resp3 in inventory):
                                        inventory.pop(resp3)
                                        print("\nDiscarded the ", resp3)
                                        break
                                    elif (resp3 not in inventory): print("\nYou don't have that!")
                    if (resp=='C'):
                        print("\nYou climb the nearest tree and get a view of the vast canopy above you.")
                        print("\nBut that's kinda useless for you as this game is text based and I cannot give a picture. (yet)")
                        fru=random.randint(2,10)
                        frut=fru
                        while fru>0:
                            inventory.append("Random Fruit")
                            fru=fru-1
                        print("\nBut while you were at it, you got", frut,"random fruits!")
                        print("\nDon't worry, these are edible.")
                        smt=random.randint(1,5)
                        if (smt==4):
                            print("\nOn your way down, you fall off the tall tree to your death.")
                            hp=0
                            
                    if (resp=='F'):
                        print("\nWhy are you wasting your time here? This option is useless in this forest, where all the good stuff is up there in the trees.")
                print("\nYou Died!")
                print("\nYou survived for", t, "turns.")
        elif (spt==2):
                print("You spawn right on top of a volcano.")
                print("What? Were you expecting a prompt asking you what you wanted to do?")
                print("Too bad that's not happening, for your luck has brought you right over this hot mountain.")
                print("You fall straight into the volcano to your death, to nobody's surprise.")
                time.sleep(3)
                print("Or did you?")
                print("You didn't die, but this location has not been made yet, so you cannot play. Please restart the game to play.")
        elif (spt==3):
                print("You spawn in the middle of a barren desert.")
                print("There doesn't seem to be much around here, except for sand. But i'm sure I did not have to tell you that last bit.")
                resp=input("What will you do? (Walk [W]||Check Inventory [I]||Find shelter [S]||Forage [F]  (RESPONSES ARE CASE SENSITIVE): ")
                print("Uhh this game isn't actually finished yet...")
                print("But I don't want to leave you in suspense, so i'll instead annoy you >:)")
                print("You Died! Please restart the game to play again.")
        elif (spt==4):
                print("You spawn in a grassland, specificially one with some of the greenest grass you've ever seen, which isn't saying a lot as you just spawned.")
                print("But hey, this ain't a bad spawn!")
                resp=input("What will you do? (Walk [W]||Check Inventory [I]||Murder an animal [M]||Forage [F]  (RESPONSES ARE CASE SENSITIVE): ")
                print("Well no doing ANYTHING in this peaceful (cough) grassland today, because this game is not finished!")
                print("You Died! Please restart the game to play again.")
        elif (spt==5):
                print("You spawn in a snowy tundra and your eyes are filled with white.")
                print("In fact, it's so snowy and cold the water vapours from your breath are causing icicles to form right underneath your nostrils.")
                print("WITHIN MILLISECONDS OF YOUR SPAWNING.")
                print("But anyways")
                resp=input("What will you do? (Walk [W]||Check Inventory [I]||Make a fire [R]||Forage [F])  (RESPONSES ARE CASE SENSITIVE): ")
                print("I'm sure you picked the third option, to no one's surprise. What else would you do in such an environment?")
                print("If you did not pick that option, I'm actually surprised. We need to talk, for I must understand your logic.")
                print("But whatever you pick will not change your outcome, for this game is not finished.")
                print("You Died! Please restart the game to play again.")


                
                

        else:
                print("Looks like this game is so unfinished your character didn't even spawn >:)")
        pl=input("Would you like to play again? (Yes [Y] ||No [N]): ")
        if pl=="Y":
                continue
        elif pl=='N':
                exit()
