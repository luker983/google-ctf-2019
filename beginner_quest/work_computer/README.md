# Work Computer (sandbox)

## Prompt

Having found the information you were looking for, while detailed, it presents you with an interesting dilemma. There is a network of "computers" not completely dissimilar to your computrator-machine on your ship. You find yourself in possession of the credentials of an individual on the planet named "SarahH." Great, with these you can get right into the secret world of an earthling without them knowing you're there. You access "SarahH home network," to find two computers: "work" and "home." Not knowing what either of these are, you have to make a decision.

With the confidence of conviction and decision making skills that made you a contender for Xenon's Universal takeover council, now disbanded, you forge ahead to the work computer.   This machine announces itself to you, surprisingly with a detailed description of all its hardware and peripherals. Your first thought is "Why does the display stand need to announce its price? And exactly how much does 999 dollars convert to in Xenonivian Bucklets?" You always were one for the trivialities of things.

Also presented is an image of a fascinating round and bumpy creature, labeled "Cauliflower for cWo" - are "Cauliflowers" earthlings?  Your 40 hearts skip a beat - these are not the strange unrelatable bipeds you imagined earthings to be.. this looks like your neighbors back home. Such curdley lobes. Will it be at the party?

SarahH, who appears to be  a programmer with several clients, has left open a terminal.  Oops.  Sorry clients!  Aliens will be poking around attempting to access your networks.. looking for Cauliflower.   That is, *if* they can learn to navigate such things.

## Files

* `flag.txt`: The solution to this challenge

## Solution

The prompt gives us a link and a port, so let's try connecting with `netcat`:

```
nc readme.ctfcompetition.com 1337
```

This greets us with a prompt:

```
                                                                                            
******************************************


        ****ALIEN SHELL****



******************************************


USER is: @(null)
>
```

Since this is a sandbox challenge, we will probably need to mess around in this shell until we find something that works. I started by trying to figure out what commands I might have. `ls` works right off the bat, showing two files: `ORME.flag` and `README.flag`. Surely it's not that easy, but let's try to print it anyway. `cat`, `less`, `vi`, `vim`, etc........ no success. Okay, our binary selection is very limited, so let's try and find out what binaries are available to us. Some good places to look are in `/bin`, `/sbin`, `/usr/bin`, and `/usr/sbin`.

There are so many options! but all we need is one binary that will let us read the flag. After looking at many of the binaries, I decided to take a brute-force approach and start running each one and trying `-h` and `help` arguments to see if I was just unfamiliar with a present print command. Most binaries were pretty standard, but one in `/bin` caught my eye: `makemime`. 

Running `makemime -h`:

```
> makemime -h
makemime: unrecognized option: h
BusyBox v1.29.3 (2019-01-24 07:45:07 UTC) multi-call binary.

Usage: makemime [OPTIONS] [FILE]...

Create multipart MIME-encoded message from FILEs

        -o FILE Output. Default: stdout
        -a HDR  Add header(s). Examples:
                "From: user@host.org", "Date: `date -R`"
        -c CT   Content type. Default: application/octet-stream
        -C CS   Charset. Default: us-ascii

Other options are silently ignored
```

Interesting, this program creates an encoded message from a file and outputs it to stdout. That sounds promising! Let's try it!

```
> makemime README.flag
Mime-Version: 1.0
Content-Type: multipart/mixed; boundary="1666536202-1266460509-2016949637"

--1666536202-1266460509-2016949637
Content-Type: application/octet-stream; charset=us-ascii
Content-Disposition: inline; filename="README.flag"
Content-Transfer-Encoding: base64

Q1RGezRsbF9ENDc0XzVoNGxsX0IzX0ZyMzN9Cg==
--1666536202-1266460509-2016949637--
```

The second line from the bottom looks like base64, and the Content-Transfer-Encoding field certainly suggest that it is base64. Decoding this gives us the flag!

```
echo Q1RGezRsbF9ENDc0XzVoNGxsX0IzX0ZyMzN9Cg== | base64 -D
CTF{4ll_D474_5h4ll_B3_Fr33}
```
