import time

def perform_cpr(person_type):
    compressions = 0
    start_time = None

    while True:
        if start_time is not None:
            elapsed_time = time.time() - start_time
            print(f"Compressions: {compressions}   Elapsed Time: {elapsed_time:.1f} seconds")

        if compressions == 0:
            print("1. Check the scene to ensure it's safe.")
            print("2. Call 911 or your local emergency number for help.")
            print("3. Place the person on their back on a firm surface.")
            if person_type == "adult":
                print("4. Check for a response (tap and shout).")
                print("5. If unresponsive, open the airway (tilt head, lift chin).")
                print("6. Check for normal breathing (look, listen, feel) for no more than 10 seconds.")
                print("7. If not breathing normally, give rescue breaths.")
                print("   - To give rescue breaths to an adult:")
                print("     - Pinch the person's nose closed.")
                print("     - Take a normal breath and cover the person's mouth with yours, making a seal.")
                print("     - Give two breaths, each lasting about 1 second, while watching for the chest to rise.")
                print("8. Locate the center of the person's chest, interlace hands, and perform compressions.")
                print("9. Compress hard and fast at a rate of 100-120 compressions per minute.")
                print("10. Allow the chest to recoil fully between compressions.")
                print("11. Give two rescue breaths after every 30 compressions.")
            elif person_type == "child":
                print("4. Check for a response (tap and shout).")
                print("5. If unresponsive, open the airway (tilt head, lift chin).")
                print("6. Check for normal breathing (look, listen, feel) for no more than 10 seconds.")
                print("7. If not breathing normally, give rescue breaths.")
                print("   - To give rescue breaths to a child:")
                print("     - Pinch the person's nose closed.")
                print("     - Take a normal breath and cover the child's mouth and nose with yours, making a seal.")
                print("     - Give two breaths, each lasting about 1 second, while watching for the chest to rise.")
                print("8. Locate the lower half of the sternum, and perform compressions using one or two hands.")
                print("9. Compress at a depth of about 2 inches (5 cm) for children.")
                print("10. Compress at a rate of 100-120 compressions per minute.")
                print("11. Allow the chest to recoil fully between compressions.")
                print("12. Give two rescue breaths after every 15 compressions.")
            print("\nBegin CPR now? Press ENTER")
            input()

        start_time = time.time()

        while True:
            compressions += 1
            elapsed_time = time.time() - start_time

            if person_type == "child" and compressions % 15 == 0:
                print("Give two rescue breaths. You have 5 seconds.")
                time.sleep(5)  # 5-second pause for rescue breaths
            elif person_type == "adult" and compressions % 30 == 0:
                print("Give two rescue breaths. You have 5 seconds.")
                time.sleep(5)  # 5-second pause for rescue breaths

            print(f"Compressions: {compressions}   Elapsed Time: {elapsed_time:.1f} seconds")

            time.sleep(1)

# Prompt the user to choose between adult or child CPR
person_type = input("Enter the person's type (adult/child): ")

# Call the function to start CPR
perform_cpr(person_type)
