// RED Light Input and Var

int R_1 = A0;
int R_2 = A1;
byte RED = 0;

// Green Light Input and Var

int G_1 = A2;
int G_2 = A3;
byte GREEN = 0;

// Blue Light Input and Var

int B_1 = A4;
int B_2 = A5;
byte BLUE = 0;

// Basic Var

byte i;
byte del = 10;

//==========================================| Setup |==========================================

void setup() {

  pinMode(R_1, OUTPUT);
  pinMode(R_2, OUTPUT);

  pinMode(G_1, OUTPUT);
  pinMode(G_2, OUTPUT);

  pinMode(B_1, OUTPUT);
  pinMode(B_2, OUTPUT);
}

//==========================================| LOOP |==========================================

void loop() {

  //----------------------------------------| Anumation 1 |----------------------------------------

  // Red High
  for (i = 0; i <= 255;) {
    analogWrite(R_1, RED);
    analogWrite(R_2, RED);
    delay(del);
    i++;
    RED++;
  }

  // Red Low
  for (i = 0; i <= 255;) {
    analogWrite(R_1, RED);
    analogWrite(R_2, RED);
    delay(del);
    i++;
    RED--;
  }

  // Green High
  for (i = 0; i <= 255;) {
    analogWrite(G_1, GREEN);
    analogWrite(G_2, GREEN);
    delay(del);
    i++;
    GREEN++;
  }

  // Green Low
  for (i = 0; i <= 255;) {
    analogWrite(G_1, GREEN);
    analogWrite(G_2, GREEN);
    delay(del);
    i++;
    GREEN--;
  }

  // Blue High
  for (i = 0; i <= 255;) {
    analogWrite(B_1, BLUE);
    analogWrite(B_2, BLUE);
    delay(del);
    i++;
    BLUE++;
  }

  // Blue Low
  for (i = 0; i <= 255;) {
    analogWrite(B_1, BLUE);
    analogWrite(B_2, BLUE);
    delay(del);
    i++;
    BLUE--;
  }

  //----------------------------------------| Anumation 2 |----------------------------------------

  // Red High
  for (i = 0; i <= 255;) {
    analogWrite(R_1, RED);
    analogWrite(R_2, RED);
    delay(del);
    i++;
    RED++;
  }

  // Green High
  for (i = 0; i <= 255;) {
    analogWrite(G_1, GREEN);
    analogWrite(G_2, GREEN);
    delay(del);
    i++;
    GREEN++;
  }

  // Red Low
  for (i = 0; i <= 255;) {
    analogWrite(R_1, RED);
    analogWrite(R_2, RED);
    delay(del);
    i++;
    RED--;
  }

  // Blue High
  for (i = 0; i <= 255;) {
    analogWrite(B_1, BLUE);
    analogWrite(B_2, BLUE);
    delay(del);
    i++;
    BLUE++;
  }

  // Green Low
  for (i = 0; i <= 255;) {
    analogWrite(G_1, GREEN);
    analogWrite(G_2, GREEN);
    delay(del);
    i++;
    GREEN--;
  }

  // Red High
  for (i = 0; i <= 255;) {
    analogWrite(R_1, RED);
    analogWrite(R_2, RED);
    delay(del);
    i++;
    RED++;
  }

  // Blue Low
  for (i = 0; i <= 255;) {
    analogWrite(B_1, BLUE);
    analogWrite(B_2, BLUE);
    delay(del);
    i++;
    BLUE--;
  }

  // Red Low
  for (i = 0; i <= 255;) {
    analogWrite(R_1, RED);
    analogWrite(R_2, RED);
    delay(del);
    i++;
    RED--;
  }

  //----------------------------------------| Anumation 3 |----------------------------------------

  // Red High | Green High
  for (i = 0; i <= 255;) {
    analogWrite(R_1, RED);
    analogWrite(R_2, RED);
    analogWrite(G_1, GREEN);
    analogWrite(G_2, GREEN);
    delay(del);
    i++;
    RED++;
    GREEN++;
  }

  // Red Low | Green Low
  for (i = 0; i <= 255;) {
    analogWrite(R_1, RED);
    analogWrite(R_2, RED);
    analogWrite(G_1, GREEN);
    analogWrite(G_2, GREEN);
    delay(del);
    i++;
    RED--;
    GREEN--;
  }

  // Green High | Blue High
  for (i = 0; i <= 255;) {
    analogWrite(G_1, GREEN);
    analogWrite(G_2, GREEN);
    analogWrite(B_1, BLUE);
    analogWrite(B_2, BLUE);
    delay(del);
    i++;
    GREEN++;
    BLUE++;
  }

  // Green Low | Blue Low
  for (i = 0; i <= 255;) {
    analogWrite(G_1, GREEN);
    analogWrite(G_2, GREEN);
    analogWrite(B_1, BLUE);
    analogWrite(B_2, BLUE);
    delay(del);
    i++;
    GREEN--;
    BLUE--;
  }

  // Red High | Blue High
  for (i = 0; i <= 255;) {
    analogWrite(G_1, RED);
    analogWrite(G_2, RED);
    analogWrite(B_1, BLUE);
    analogWrite(B_2, BLUE);
    delay(del);
    i++;
    RED++;
    BLUE++;
  }

  // Red Low | Blue Low
  for (i = 0; i <= 255;) {
    analogWrite(G_1, RED);
    analogWrite(G_2, RED);
    analogWrite(B_1, BLUE);
    analogWrite(B_2, BLUE);
    delay(del);
    i++;
    RED--;
    BLUE--;
  }

  //----------------------------------------| Anumation 4 |----------------------------------------

  for (i = 0; i<=255;) {
    analogWrite(G_1, RED);
    analogWrite(G_2, RED);
    analogWrite(B_1, GREEN);
    analogWrite(B_2, GREEN);
    analogWrite(G_1,  BLUE);
    analogWrite(G_2,  BLUE);
    delay(del);
    i++;
    RED++;
    GREEN++;
    BLUE++;
  }

  for (i = 0; i<=255;) {
    analogWrite(G_1, RED);
    analogWrite(G_2, RED);
    analogWrite(B_1, GREEN);
    analogWrite(B_2, GREEN);
    analogWrite(G_1,  BLUE);
    analogWrite(G_2,  BLUE);
    delay(del);
    i++;
    RED--;
    GREEN--;
    BLUE--;
  }

}