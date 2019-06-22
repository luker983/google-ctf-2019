# Satellite (networking) 

## Prompt

Having successfully figured out this "coordinate" problem. The ship lurches forward violently into space. This is one of the moments when you realize that some kind of thought or plan would have been good, but typically for you and how you found yourself in this situation, you didn't think too much before acting. Only the stars themselves know where you'll end up.

After what seems like an eternity, or at least one full season of "Xenon's Next Top Galactic Overlord" you arrive in a system of 9 planetary bodies, though one of them is exceptionally small. You nostalgically remember playing explodatoid with your friends and hunting down planets like this. But this small planet registers a hive of noise and activity on your ships automated scanners. There's things there! Billions upon trillions of things, moving around, flying, swimming, sliding, falling.

Of particular interest may be the insect-like creatures flying around this planet, uniformly. One has the words "Osmium Satellites" written on it. Maybe this is a starting point to get to know what's ahead of you.

Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?

Find something to do that isn't staring at the Blue Planet.

## Steps
1. Get on a working network connection that doesn't have any proxy issues
2. Use PDF to realize that you need to connect to `osmium` satellite
3. Get configuration from website
4. Copy Base64 text and then run `echo base_64_text | base64 -d`
5. Realize you have to sniff the traffic
6. Run `sudo tcpdump -i [interface] -A src 34.76.101.29`
