def cow(eyes="oo", tongue=" "):
    return (
f"""      o  ^__^             
       o ({eyes})\________    
         (__)\        )\/\\
          {tongue}   ||----w |   
              ||     ||   """)

def cowponder(mode=""):
    faces = dict(
       b=("==", " "),
       d=("XX", "U"),
       g=("$$", " "),
       p=("@@", " "),
       s=("**", "U"),
       y=("..", " ")
    )
    if mode:
        args = faces[mode[-1]]
    return cow(*args)