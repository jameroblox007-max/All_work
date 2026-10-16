import os

def check_files_in_directory(path):
    if not os.path.exists(path):
        print("ไม่พบโฟลเดอร์นี้")
        return

    all_entries = os.listdir(path)

    total_size_all = 0
    total_size_images = 0
    image_files = []

    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')

    print(f"=== รายชื่อไฟล์ทั้งหมดใน: {path} ===")
    
    for name in all_entries:
        full_path = os.path.join(path, name)

        if os.path.isfile(full_path):
            file_size = os.path.getsize(full_path) 
            print(f"- {name} ({file_size:,} bytes)")

            total_size_all += file_size

            if name.lower().endswith(image_extensions):
                image_files.append((name, file_size))
                total_size_images += file_size

    print(f"\n---> ขนาดไฟล์ทั้งหมดรวมกัน: {total_size_all:,} bytes ({total_size_all / (1024 * 1024):.2f} MB)")


    print("=== รายชื่อเฉพาะไฟล์รูปภาพ (.jpg, .gif, .png) ===")
    
    for img_name, img_size in image_files:
        print(f"- {img_name} ({img_size:,} bytes)")

    print(f"\n---> ขนาดไฟล์รูปภาพรวมกัน: {total_size_images:,} bytes ({total_size_images / (1024 * 1024):.2f} MB)")

folder_path = "." 
check_files_in_directory(folder_path)