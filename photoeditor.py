from PIL import Image


def open_image(image_name):
    img = Image.open(image_name)
    img.show()


def crop_image(image_name):
    img = Image.open(image_name)
    left = int(input("Enter the value to crop left: "))
    up = int(input("Enter the value to crop up: "))
    right = int(input("Enter the value to crop right: "))
    down = int(input("Enter the value to crop down: "))
    box = (left, up, right, down)
    cropped_image = img.crop(box)
    override_option = input("Would you like to override the original image? (y/n): ")
    lower_override_option = override_option.lower()
    if lower_override_option == "y":
        cropped_image.save(image_name)
    elif lower_override_option == "n":
        new_name = input("Enter a new name for this image: ")
        file_type = input("Enter the file type of the image (e.g., png, jpg): ")
        new_name_with_extension = new_name + "." + file_type
        cropped_image.save(new_name_with_extension)


def resize_image(image_name):
    img = Image.open(image_name)
    size_x = int(input("Enter the value of the x-axis to resize: "))
    size_y = int(input("Enter the value of the y-axis to resize: "))
    box = (size_x, size_y)
    resized_img = img.resize(box)
    override_option = input("Would you like to override the original image? (y/n): ")
    lower_override_option = override_option.lower()
    if lower_override_option == "y":
        resized_img.save(image_name)
    elif lower_override_option == "n":
        new_name = input("Enter a new name for this image: ")
        file_type = input("Enter the file type of the image (e.g., png, jpg): ")
        new_name_with_extension = new_name + "." + file_type
        resized_img.save(new_name_with_extension)


def rotate_image(image_name):
    img = Image.open(image_name)
    rotate = int(input("Enter the value of rotation (clockwise): "))
    rotated_img = img.rotate(-rotate)
    override_option = input("Would you like to override the original image? (y/n): ")
    lower_override_option = override_option.lower()
    if lower_override_option == "y":
        rotated_img.save(image_name)
    elif lower_override_option == "n":
        new_name = input("Enter a new name for this image: ")
        file_type = input("Enter the file type of the image (e.g., png, jpg): ")
        new_name_with_extension = new_name + "." + file_type
        rotated_img.save(new_name_with_extension)


def info(image_name):
    img = Image.open(image_name)
    print()
    print(f"File name: {image_name}")
    print(f"File format: {img.format}")
    print(f"File mode: {img.mode}")
    print(f"File size: {img.size}")
    print()


def main():
    print("Please type in the file name, for example image.jpg")
    image_name = input("File name: ")
    while True:
        print("What would you like to do with this image?")
        print("1. Show image")
        print("2. Crop image")
        print("3. Resize image")
        print("4. Rotate image")
        print("5. Change image")
        print("6. View image info")
        print("7. Quit")

        choice = input("Enter an option (1-7): ")

        if choice == "1":
            open_image(image_name)
        elif choice == "2":
            crop_image(image_name)
        elif choice == "3":
            resize_image(image_name)
        elif choice == "4":
            rotate_image(image_name)
        elif choice == "5":
            print("Please type in the file name, for example image.jpg")
            change_img_name = input("Enter file name: ")
            image_name = change_img_name
        elif choice == "6":
            info(image_name)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


main()
