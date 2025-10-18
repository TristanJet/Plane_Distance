**Multiplayer Distance Guesser** 
**East to west**
*Indiana Jones graphics*

-------------
**Premise**

Room created
Room filled

Initial and Final location hand picked - limited per (5)?

Players perform *x* hops of *y* km (6, 20000km)?

Players are presented with the next airport
Players individually guess on the distance of the hop

Players are scored on closeness to actual distance

After *x* hops, player rankings are revealed

------------
**Backend**

- Create room //POST
- Join game //GET - room in query string
- On fill -> init game
    - Random on iso_country first, then airport, to give variable country each time
    - set airports + calc distances
while game
    - //POST distance guess
        - calc score
    - //GET game state
        - players guessed
        - time left
- //GET final scores
    - final player scores to display

------------
**Frontend**

- *one time* Render world map svg
    - d3js geojson to svg? [d3]('https://d3js.org/d3-geo')

- Serve svg
    - on client render co-ordinates as x, y points

