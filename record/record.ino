#define SAMPLE_BYTES 255

void setup() {
	pinMode(12, INPUT);
	pinMode(13, OUTPUT);
	Serial.begin(9600);
}

void loop() {
	uint8_t measurements[SAMPLE_BYTES];
	while (digitalRead(12) == HIGH); // wait for signal to start
	
	digitalWrite(13, HIGH);
	for (uint8_t octet = 0; octet < SAMPLE_BYTES; octet++) {
		measurements[octet] = 0;
		for (uint8_t b = 128; b != 0; b >>= 1) {
			if (digitalRead(12) == HIGH) measurements[octet] |= b;
			delayMicroseconds(48);
		}
	}

	Serial.println("-----BEGIN DUMP-----");
	for (uint8_t octet = 0; octet < SAMPLE_BYTES; octet++) {
		Serial.print(measurements[octet], HEX);
		Serial.print(" ");
	}
	Serial.println();
	Serial.println("-----END DUMP-----");

	delay(100);
	digitalWrite(13, LOW);
}
