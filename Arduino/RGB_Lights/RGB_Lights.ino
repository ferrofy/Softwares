// =======================================| Lights |=======================================

int R = 9;
int G = 10;
int B = 11;

// =======================================| Delay n Steps |=======================================

int Fade_Time = 10000;
int Steps = 255;
int Delay_Time = Fade_Time / (Steps * 2);

// =======================================| Functions |=======================================

void LED_High(int Color) {
  for (int i = 0; i <= Steps; i++) {
    analogWrite(Color, 255 - i);
    delay(Delay_Time);
  }
}

void LED_Low(int Color) {
  for (int i = Steps; i >= 0; i--) {
    analogWrite(Color, 255 - i);
    delay(Delay_Time);
  }
}

void White_Color(int Color_1, int Color_2, int Color_3) {
  for (int i = 0; i <= Steps; i++) {
    analogWrite(Color_1, 255 - i);
    analogWrite(Color_2, 255 - i);
    analogWrite(Color_3, 255 - i);
    delay(Delay_Time);
  }
  delay(Delay_Time);
  for (int i = Steps; i >= 0; i--) {
    analogWrite(Color_1, 255 - i);
    analogWrite(Color_2, 255 - i);
    analogWrite(Color_3, 255 - i);
    delay(Delay_Time);
  }
}

// =======================================| Setup |=======================================

void setup() {
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);
}

// =======================================| Loop |=======================================


void loop() {

  // White Color

  White_Color(R, G, B);

  // One to Another Color
  LED_High(R);
  LED_Low(R);
  LED_High(G);
  LED_Low(G);
  LED_High(B);
  LED_Low(B);

  // Two To Another Color
  LED_High(R);
  LED_High(G);
  LED_Low(R);
  LED_High(B);
  LED_Low(G);
  LED_High(R);
  LED_Low(B);
  LED_Low(R);

  // Three To Another Color
  LED_High(R);
  LED_High(G);
  LED_High(B);
  LED_Low(B);
  LED_Low(G);
  LED_Low(R);
  LED_High(R);
  LED_High(G);
  LED_High(B);
  LED_Low(R);
  LED_Low(G);
  LED_Low(B);
}