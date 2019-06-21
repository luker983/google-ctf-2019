# Satellite 

## Prompt
Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?

Find something to do that isn't staring at the Blue Planet.

## Steps
1. Get on a working network connection that doesn't have any proxy issues
2. Use PDF to realize that you need to connect to `osmium` satellite
3. Get configuration from website
4. Copy Base64 text and then run `echo base_64_text | base64 -d`
5. Realize you have to sniff the traffic
6. Run `sudo tcpdump -i [interface] -A src 34.76.101.29`
