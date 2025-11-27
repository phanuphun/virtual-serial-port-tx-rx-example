import time
import serial  # มาจาก pyserial

# เปิดพอร์ต COM5 (ให้ตั้ง baud ให้ตรงกับฝั่งที่รับ เช่น 9600)
ser = serial.Serial(
    port="COM5",
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1,          # รออ่านสูงสุด 1 วินาที (จะใช้/ไม่ใช้ก็ได้)
)

print("Opened:", ser.portstr)

try:
    while True:
        text = input("พิมพ์ข้อความที่จะส่ง (หรือ 'exit' เพื่อออก): ")
        if text.lower() == "exit":
            break

        # แปลงเป็น bytes แล้วส่ง
        ser.write((text + "\r\n").encode("utf-8"))
        print("ส่งแล้ว:", text)

        time.sleep(0.1)

finally:
    ser.close()
    print("ปิดพอร์ตแล้ว")
