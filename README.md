Welcome to Team ___;s 473 Clustering ERD Project!

Assumptions:
we assume that all of the possible images in Collection are in the same folder as
our python file that outputs a list of entitities and the text inside the entity.

Our python file that outputs a list of entitities and the text inside the entity
is called "final_parse.py". Run "python3 final_parse.py" to receive a list
of entities read from our outputted JSON file.

There is no separation of entities read by image; all are outputted into the same array.

Other Notes:
- "output.json" -> Json file that is read in
- "final_parse.py" -> parses json files, reads it, and outputs entity list. Assumes
   the images it is tested against are in the same folder.
- there are two modes in final_parse.py. Manual testing reads from the json, Auto testing
   reads from the xml coordinates in an array at the top of the file.