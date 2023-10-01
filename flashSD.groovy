def call(String filename,String sdx) {
 sh "sudo dd if=${filename} of=/dev/${sdx} bs=1M conv=fsync status=progress"
//  sudo dd if=ubuntucore_backup.img of=/dev/sda bs=1M conv=fsync status=progress

}
return this;