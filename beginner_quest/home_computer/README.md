# Home Computer (forensics)

## Prompt

Having found the information you were looking for, while detailed, it presents you with an interesting dilemma. There is a network of "computers" not completely dissimilar to your computrator-machine on your ship. You find yourself in possession of the credentials of an individual on the planet named "SarahH." Great, with these you can get right into the secret world of an earthling without them knowing you're there. You access "SarahH home network," to find two computers: "work" and "home." Not knowing what either of these are, you have to make a decision.

Blunderbussing your way through the decision making process, you figure that one is as good as the other and that further research into the importance of Work Life balance is of little interest to you. You're the decider after all. You confidently use the credentials to access the "Home Computer."

Something called "desktop" presents itself, displaying a fascinating round and bumpy creature (much like yourself) labeled  "cauliflower 4 work - GAN post."  Your 40 hearts skip a beat.  It looks somewhat like your neighbors on XiXaX3.   ..Ah XiXaX3... You'd spend summers there at the beach, an awkward kid from ObarPool on a family vacation, yearning, but without nerve, to talk to those cool sophisticated locals.

So are these "Cauliflowers" earthlings? Not at all the unrelatable bipeds you imagined them to be.  Will they be at the party?  Hopefully SarahH has left some other work data on her home computer for you to learn more.

## Files

* `files.zip`: Provided zip file that contains `note.txt` and `family.ntfs`.
* `note.txt`: MacOS compatibility note.
* `family.ntfs`: Filesystem binary.
* `credentials.txt`: Hint to find credentials.
* `credentials_extended_hex.out`: Extended attribute of `credentials.txt` in hex.
* `output.png`: `credentials_extended_hex.out` converted to PNG.
* `flag.txt`: Solution to this challenge.

## Solution

A quick google search for `NTFS` reveals that the acronym stands for NT File System. `file` on the binary confirms this:

```
$ file family.ntfs
family.ntfs: DOS/MBR boot sector, code offset 0x52+2, OEM-ID "NTFS    ", sectors/cluster 8, Media descriptor 0xf8, sectors/track 0, dos < 4.0 BootSector (0x80), FAT (1Y bit by descriptor); NTFS, sectors 51199, $MFT start cluster 4, $MFTMirror start cluster 3199, bytes/RecordSegment 2^(-1*246), clusters/index block 1, serial number 072643f694104cb6f
```

Let's try mounting it! 

```
mkdir -p /mnt/ntfs && mount ./family.ntfs /mnt/ntfs
```

This seems to have worked. A good first step when getting on a new machine is to look in the home folders for interesting files like password backups or SSH keys. Searching around `Users/Family` reveals a ton of interesting files, mostly interesting file names that are empty. However, `Users/Family/Documents` has a file with some content: `credentials.txt`.

```
I keep pictures of my credentials in extended attributes.
```

Now we have a lead. After a bit of research, it appears that extended attributes are like metadata, information stored alongside the file, but not inside the file itself. Let's see if the `credentials.txt` file has any of these extended attributes:

```
$ getfattr credentials.txt
# file: credentials.txt
user.FILE0

```

That looks like an extended attribute to me. `man getfattr` to find out how to read it. I chose to output to hex, then convert from hex to binary, but I know some people found a flag that would output the binary right away. 

```
getfattr -e hex -n user.FILE0 credentials.txt > credentials_extended_hex.out
```

Now the output needs to be cleaned up. There are a few extra characters that need to be removed from the beginning:
```
# file: credentials.txt
user.FILE0=
```
 
Now the hex can be reversed!

```
xxd -r -p credentials_extended_hex.out output
```

Running `file` on the output shows that it's a PNG, so opening it up as a PNG with `xdg-open output.png` gives us the flag!

![Extended Attribute](output.png "Img")
