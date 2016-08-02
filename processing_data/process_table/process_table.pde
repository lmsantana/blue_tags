
/*
  Program made to rtanslate the table of tags for a visual interface
  Lucas Moura Santana
  01 Aug 2016
*/

Table table;
int[][] presence = new int[3][200];

String initial_time;
String final_time;
String name;
String time;
int counter;

PFont f;

void setup() {
  size(1200,900);
  noStroke();
  f = createFont("Arial", 24, true);
  
  table = loadTable("data_from_rpi_at_2016_08_01__15_35_35.csv", "header");
  println(table.getRowCount() + " total rows in table");
  
  for (TableRow row : table.rows()) {
    
    name = row.getString("name");
    time = row.getString("time");
    counter = row.getInt("counter");
    
    if (counter == 1) {
      initial_time = time;
    }
    
    if (name.equals("Austin")) {
      presence[0][counter] = 1;
    }
    else if (name.equals("Haley")) {
      presence[1][counter] = 1;
    }
    else if (name.equals("Jose")) {
      presence[2][counter] = 1;
    }
      
    
    //println(name + time + " " + str(counter));
  }
  final_time = time;
  for (int i = 0; i <3; i++) {
    for (int j = 0; j < 200; j++) {
      print(presence[i][j]);
    }
    println(" ");
  }   
}

void draw(){
  background(255);
  textFont(f);
  fill(0);
  
  // Writing names and labels
  text("Presence of tags near sensor over time", 350,90);
  
  text("Austin", 100, 270);
  text("Haley", 100, 450);
  text("Jose", 100, 630);
  
  // Time frame lines
  text(initial_time, 150, 810);
  line(200, 100, 200, 700);
  text(final_time, 900, 810);
  line(1000, 100, 1000, 700);
  
  // Blocks of time presence drawing
  stroke(1);
  fill(#00FF00);
  for (int i = 0; i <3; i++) {
    for (int j = 0; j < 200; j++) {
      if (presence[i][j] == 1) {
        //rect(150 + 3*j + 0, 260 +180*i, 150+ 3*j + 2, 280 +180*i);
        rect(200 + 4*j, 240 + 180*i, 4,60);
      }
    }
  }
  
  
}