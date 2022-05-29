# byuCTF Reconstruct

In the challenge "Reconstruct" we were given a .png file and a MD5-Hash for verification.
We can start by opening the PNG file. We see some text and whats supposed to be a censored flag.
On the bottom of the PNG we find the letter a-z and numbers 0-9. This implies, that the contents of the flag are composed of these characters. So we can assume, that there aren't any uppercase letters. I opened the picture in GIMP and tried to enhance the quality or remove the black bar. I couldn't remove the blöack bar, but i sharpened thge edges and played with some color curves, to enhance the edges on the text.

Now we can begin to reconstruct the flag's contents.
First i wrote down the layout of the flag:
byuctf{????_????_???_????????_??_????_?_???_???????????_??}
abcdefghijklmnopqrstuvwxyz0123456789
The flag layout looked like this
First i wanted to know the character which had the flat bottom and could be seen above the black bar.
This character turned out to be the number "1"
byuctf{????_?1??_???_?1??????_??_1???_1_???_???????????_1?}
We can erase the number 1 from our character set, because all 1's were mapped to the flag.
abcdefghijklmnopqrstuvwxyz023456789
We can remove the letters from the character set, that go below our underscores, like "gjpqy".
Our new character set looks like this:
abcdefhiklmnorstuvwxz023456789
Let's focus on all the letters that rise above the black bar.
For this we can search the tallest letters in the character set. Those are "bdfhkl" Notice, that the letter t isn't as tall as the other tall characters, so the letter t most likely wouldn't rise above the black bar.
We can map these tall characters to the flag, if we look on the shape above and below the black bar. Our flag looks like this now:
byuctf{????_?1?h_?h?_l1??l???_?f_1?f?_1_???_???????????_1?}
Our new character set looks like this
aceimnorstuvwxz023456789
Notice that all the numbers that are left are also tall characters which should rise above the black bar. So we can remove them as well, because we mapped all of the flags tall characters.
aceimnorstuvwxz
I have the feeling the letter t is in our flag, so lets have a look ath the letter t's shape. It shouldn't rise above the black bar and has a little hook like shape on the bottom. So let's see where it could fit in.
byuctf{????_?1th_th?_l1ttl??t_?f_1?f?_1_???_??????t???t_1t}
Now we see some words form. the word "?1th" could be "w1th" and the word "th?" is most probably the word "the". Now we can find the rest of the "w" and "e" letters in the flag. We just have to compare their shapes with some characters in the flag.
byuctf{e?e?_w1th_the_l1ttle?t_?f_1?f?_1_???_?e????t???t_1t}
Our new character set looks like this
acimnorsuvxz
We can also assume, that the 1 replaces every i in the flag. So we can remove the i from our character set.
acmnorsuvxz
We can guess 2 other words in the flag. the first one is "l1ttlest" and the second one is "of" So we can compare the shapes of s and o with the remaining characters in the flag.
byuctf{e?e?_w1th_the_l1ttlest_of_1?fo_1_???_?e?o?st???t_1t}
The word "1?fo" looks like "1nfo", so we can fill in the n's like before.
byuctf{e?en_w1th_the_l1ttlest_of_1nfo_1_??n_?e?onst???t_1t}
The first word looks like the word "even", so we can remove v from our character set.
acmruxz
byuctf{even_w1th_the_l1ttlest_of_1nfo_1_??n_?e?onst???t_1t}
The only letter in our cahracter set which has a little hook on the bottom is the c so we can fill in the c
byuctf{even_w1th_the_l1ttlest_of_1nfo_1_c?n_?econst??ct_1t}
amruxz
The character r is the only character left in our set, which has a straight point like shape on the bottom, so we can fill in the r in our flag.
byuctf{even_w1th_the_l1ttlest_of_1nfo_1_c?n_reconstr?ct_1t}
amuxz
The only shapes in the flag that are left, are the a and the u, if we compare them to our character set.
So now we have the flag:
byuctf{even_w1th_the_l1ttlest_of_1nfo_1_can_reconstruct_1t}
If we compare the MD5 Hash of our flag with the one provided to us, we can check if the flag is correct. And indeed the flag we reconstructed matches the correct answer.