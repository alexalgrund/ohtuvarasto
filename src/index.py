from varasto import Varasto


def main():
    mehua, olutta = Varasto(100.0), Varasto(100.0, 20.2)

    print(f"""
  Mehuvarasto: {mehua}
  Olutvarasto: {olutta}

Olut getterit:
  saldo={olutta.saldo}, tilavuus={olutta.tilavuus},
  paljonko_mahtuu={olutta.paljonko_mahtuu()}

Mehu setterit:
  Lisätään 50.7 -> {mehua.lisaa_varastoon(50.7) or mehua}
  Otetaan 3.14 -> saatiin {mehua.ota_varastosta(3.14)}, nyt {mehua}

Olutvarasto:
  Lisätään 1000.0 -> {olutta.lisaa_varastoon(1000.0) or olutta}
  Otetaan 1000.0 -> saatiin {olutta.ota_varastosta(1000.0)}, nyt {olutta}

Mehuvarasto:
  Lisätään -666.0 -> {mehua.lisaa_varastoon(-666.0) or mehua}
  Otetaan -32.9 -> saatiin {mehua.ota_varastosta(-32.9)}, nyt {mehua}
""")


if __name__ == "__main__":
    main()
