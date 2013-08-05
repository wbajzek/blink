blink
=====

Process status utility for [Blinkstick](http://blinkstick.com/). It will pulse white 
while your process is going and then light up red or green depending on the outcome. 
Then you can press enter to turn it off. I use it for processes that take a long time, 
like running automated tests.
~~~
blink "rspec spec && cucumber"
~~~
The initial code for this was derived from https://github.com/arvydas/blinkstick-python. 
You will need to install libusb and blinkstick as described in his readme. Then make it 
executable and copy or symlink it to ~/bin. 
~~~
chmod +x blink.py
cp blink.py ~/bin/blink
~~~
Symlink didn't work for me; I got a "too many levels of symlinks" error probably because
my python was installed with homebrew and is a symlink itself.
