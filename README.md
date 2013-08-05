blink
=====

Process status utility for Blinkstick. Make it executable and copy it to bin:
~~~
chmod +x blink.py
cp blink.py ~/bin/blink
~~~
You ought to be able to symlink it but I got a "too many levels of symlink"
error.

It will pulse white while your process is going and then light up red or green
depending on the outcome. Then you can press enter to turn it off. I use it for
processes that take a long time, like running automated tests.
~~~
blink "rspec spec && cucumber"
~~~
