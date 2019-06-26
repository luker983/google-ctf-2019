# FriendSpaceBookPlusAllAccessRedPremium.com (reversing)

## Prompt

Having snooped around like the expert spy you were never trained to be, you found something that takes your interest: "Cookie/www.FriendSpaceBookPlusAllAccessRedPremium.com"  But unbeknownst to you, it was only the  700nm Wavelength herring rather than a delicious cookie that you could have found.   It looks exactly like a credential for another system.  You find yourself in search of a friendly book to read.

Having already spent some time trying to find a way to gain more intelligence... and learn about those fluffy creatures, you (several)-momentarily divert your attention here.  It's a place of all the individuals in the world sharing large amounts of data with one another. Strangely enough, all of the inhabitants seem to speak using this weird pictorial language. And there is hot disagreement over what the meaning of an eggplant is.

But not much Cauliflower here.  They must be very private creatures.  SarahH has left open some proprietary tools, surely running this will take you to them.  Decipher this language and move forth!

## Files

* `files.zip` provided zip file that contains `vm.py` and `program`
* `vm.py` stack based virtual machine that takes emojis as input
* `program` emoji program that seems to be trying to print out a URL

## Solution

Running the program with `python3 vm.py program` starts to print out what looks like a URL:

```
http://emoji-t0anaxn
```

But it seems like it will take a long time to finish. `program` is full of emojis, so let's jump to the `vm.py` file to figure out exactly what the emojis mean:

```
'🍡': add,
'🤡': clone,
'📐': divide,
'😲': if_zero,
'😄': if_not_zero,
'🏀': jump_to,
'🚛': load,
'📬': modulo,
'⭐': multiply,
'🍿': pop,
'📤': pop_out,
'🎤': print_top,
'📥': push,
'🔪': sub,
'🌓': xor,
'⛰': jump_top,
'⌛': exit
``` 

This key helps, but there are still lots of emojis like `🥇` and `✋` that are not here. Those can be found by looking at the `load` function code. Another confusing set of emojis that may not be obvious are groupings that look like this:

```
🖋💠🏁🎌🔶🚩
```

The 🖋 marks the beginning of an assembly-like label. The flags that follow are unique so that this spot can be jumped to in the future. `🏀` jumps to the label after `💰`. `hello_world` shows how jumps and labels can be used to pop and print everything off of the stack. 

 

1. Make file containing all stack values from accumulator 1
2. print out `xor` values to see pattern
3. write program that will calculate 1000 palindromic primes
4. write program to `xor` stack values and palindromic primes
5. go to `link.txt` and view one of the profiles
