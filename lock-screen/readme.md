# Lock screen

> Take a look! We found an utilized *gavphone*! Nevertheless, we have a trouble. It is protected by four-digit code. We provide you secure remote connection to the phone. Just log into it.
>
> Connect to server: `nc ctf.upml.tech 1234`
>
> _Note:_ if you're using Windows, you can connect via Putty in Raw mode

## Write-up

Let's store all valid codes.

On each step use first valid code, and remove all codes which are inconsistent with one of previous answers.

Jury tested it many times and, according to statistics, it will remove at least 2/3 of available codes on each step (usually around 80%).
It means that for 5 040 valid codes at start we need at most 7-9 tries (if we're unlucky).
But [author's solution](https://github.com/upmlctf/2017-quals/blob/master/lock-screen/solution.py) has never failed (for 1 000 runs).

After 15 guesses, team will get flag.

Flag: `uctfimp0ssibletosolve`
