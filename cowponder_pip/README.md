# Cowponder

A simple terminal command that displays randomly selected philosophical thoughts from a cow

[cowponder website](https://max.xz.ax/cowponder/)
```text
 ______________________________________
( squeezing an ounce of meaning out of )
( this world                           )
 --------------------------------------
        o   ^__^
         o  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Usage

After installation, the thoughtbook must be initialized.
We recommend running `cowponder --update` with root privileges
so that the generated thoughtbook file can be shared;
otherwise, cowponder will use a user-local thoughtbook.

```bash
# displays a thought
ponder

# displays a thought from a cow
cowponder
```

Cowponder can also be imported into python code:
```
>>> from cowponder.ponder import cowponder
>>> print(cowponder())
 _______________________________________
( the realm of better days eats away my )
( mind                                  )
 ---------------------------------------
      o  ^__^             
       o (oo)\________    
         (__)\        )\/\
              ||----w |   
              ||     ||   
```

Note: the internal python API is unstable and may be subject to change.