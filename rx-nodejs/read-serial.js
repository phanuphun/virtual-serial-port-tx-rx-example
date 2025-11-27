import { SerialPort } from 'serialport'
import { ReadlineParser } from '@serialport/parser-readline'

const port = new SerialPort({
  path: 'COM6',
  baudRate: 9600,
  dataBits: 8,
  parity: 'none',
  stopBits: 1,
  autoOpen: false,
})

// parser เอาไว้ตัดบรรทัดด้วย \r\n ให้สวย ๆ
const parser = port.pipe(new ReadlineParser({ delimiter: '\r\n' }))

port.open(err => {
  if (err) {
    console.error('เปิดพอร์ตไม่ได้:', err.message)
    return
  }
  console.log('✅ เปิดพอร์ต COM6 แล้ว (รอฟังข้อมูล...)')
})

parser.on('data', line => {
  console.log('📥 รับข้อมูล:', line)
})

port.on('error', err => {
  console.error('Serial error:', err)
})
