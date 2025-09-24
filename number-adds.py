def convert_numbers_to_vcf_batches(txt_filename='numbers.txt', batch_size=10000):
    try:
        with open(txt_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"فایل {txt_filename} یافت نشد.")
        return

    contacts = []
    for idx, line in enumerate(lines, start=1):
        phone = line.strip()
        if not phone:
            continue

        if not (phone.isdigit() or (phone.startswith('+') and phone[1:].isdigit())):
            print(f"شماره نامعتبر در خط {idx}: {phone}")
            continue

        name = f"kir{idx}"
        contacts.append((name, phone))

    if not contacts:
        print("شماری برای تبدیل یافت نشد.")
        return

    file_count = 1
    for i in range(0, len(contacts), batch_size):
        batch = contacts[i:i + batch_size]
        vcf_filename = f'contacts_part_{file_count}.vcf'

        with open(vcf_filename, 'w', encoding='utf-8') as f:
            for name, phone in batch:
                vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
END:VCARD

"""
                f.write(vcard)

        print(f"فایل {vcf_filename} ساخته شد با {len(batch)} مخاطب.")
        file_count += 1


if __name__ == '__main__':

    convert_numbers_to_vcf_batches()
