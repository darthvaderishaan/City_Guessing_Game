import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("City Guessing Game")

# Font settings
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 32)  # Font for the input box

# City and country data
city_country_mapping = {
    "New York City": "United States",
    "Los Angeles": "United States",
    "Chicago": "United States",
    "Houston": "United States",
    "Miami": "United States",
    "San Fransisco": "United States",
    "London": "United Kingdom",
    "Manchester": "United Kingdom",
    "Birmingham": "United Kingdom",
    "Glasgow": "United Kingdom",
    "Liverpool": "United Kingdom",
    "Edinburgh": "United Kingdom",
    "Paris": "France",
    'Marseille': "France",
    'Lyon': "France",
    'Toulouse': "France",
    'Nice': "France",
    'Bordeaux': "France",
    'Berlin': "Germany",
    'Hamburg': "Germany",
    'Munich': "Germany",
    'Cologne': "Germany",
    'Frankfurt': "Germany",
    'Dusseldorf': "Germany",
    'Tokyo': "Japan",
    'Osaka': "Japan",
    'Kyoto': "Japan",
    'Yokohama': "Japan",
    'Sapporo': "Japan",
    'Nagoya': "Japan",
    'Delhi': 'India',
    'Mumbai': 'India',
    'Bangalore': 'India',
    'Chennai': 'India',
    'Kolkata': 'India',
    'Hyderabad': 'India',
    'Sydney': 'Australia',
    'Melbourne': 'Australia',
    'Brisbane': 'Australia',
    'Perth': 'Australia',
    'Adelaide': 'Australia',
    'Canberra': 'Australia',
    'Toronto': 'Canada',
    'Vancouver': 'Canada',
    'Montreal': 'Canada',
    'Calgary': 'Canada',
    'Ottawa': 'Canada',
    'Edmonton': 'Canada',
    'Sao Paulo': 'Brazil',
    'Rio de Janeiro': 'Brazil',
    'Brasilia': 'Brazil',
    'Salvador': 'Brazil',
    'Fortaleza': 'Brazil',
    'Manaus': 'Brazil',
    'Beijing': 'China',
    'Shanghai': 'China',
    'Guangzhou': 'China',
    'Shenzhen': 'China',
    'Chengdu': 'China',
    'Hangzhou': 'China',
    'Johannesburg': 'South Africa',
    'Cape Town': 'South Africa',
    'Durban': 'South Africa',
    'Pretoria': 'South Africa',
    'Port Elizabeth': 'South Africa',
    'Bloemfontein': 'South Africa',
    'Moscow': 'Russia',
    'Saint Petersburg': 'Russia',
    'Novosibirsk': 'Russia',
    'Yekaterinburg': 'Russia',
    'Kazan': 'Russia',
    'Sochi': 'Russia',
    'Mexico City': 'Mexico',
    'Guadalajara': 'Mexico',
    'Monterrey': 'Mexico',
    'Puebla': 'Mexico',
    'Tijuana': 'Mexico',
    'Cancun': 'Mexico',
    'Rome': 'Italy',
    'Milan': 'Italy',
    'Naples': 'Italy',
    'Turin': 'Italy',
    'Palermo': 'Italy',
    'Florence': 'Italy',
    'Madrid': 'Spain',
    'Barcelona': 'Spain',
    'Valencia': 'Spain',
    'Seville': 'Spain',
    'Zaragoza': 'Spain',
    'Bilbao': 'Spain',
    'Seoul': 'South Korea',
    'Busan': 'South Korea',
    'Incheon': 'South Korea',
    'Daegu': 'South Korea',
    'Daejeon': 'South Korea',
    'Gwangju': 'South Korea',
    'Lagos': 'Nigeria',
    'Kano': 'Nigeria',
    'Ibadan': 'Nigeria',
    'Abuja': 'Nigeria',
    'Port Harcourt': 'Nigeria',
    'Benin City': 'Nigeria',
    "Cairo": 'Egypt',
    'Alexandria': 'Egypt',
    'Giza': 'Egypt',
    'Shubra El Kheima': 'Egypt',
    'Port Said': 'Egypt',
    'Suez': 'Egypt',
    'Auckland': 'New Zealand',
    'Wellington': 'New Zealand',
    'Christchurch': 'New Zealand',
    'Hamilton': 'New Zealand',
    'Tauranga': 'New Zealand',
    'Dunedin': 'New Zealand',
    'Buenos Aires': 'Argentina',
    'Cordoba': 'Argentina',
    'Rosario': 'Argentina',
    'Mendoza': 'Argentina',
    'La Plata': 'Argentina',
    'San Miguel de Tucumán': 'Argentina',
}

def get_random_city():
    if city_country_mapping:
        return random.choice(list(city_country_mapping.keys()))
    else:
        print("City-country mapping dictionary is empty. Please ensure it contains data.")
        pygame.quit()
        sys.exit()

def is_close(guess, actual):
    return guess.lower() == actual.lower()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def draw_button(rect, color, text, text_color):
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main():
    print("Welcome to the City Guessing Game!")
    print("Try to guess the country of the mystery city.")

    mystery_city = get_random_city()
    mystery_country = city_country_mapping[mystery_city]

    input_box = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()

    try_again_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 50, 100, 50)
    next_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50)
    quit_button = pygame.Rect(WIDTH // 4 * 3 - 50, HEIGHT // 2 + 50, 100, 50)

    correct_answer = False
    incorrect_message = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

                if try_again_button.collidepoint(event.pos):
                    text = ''
                    incorrect_message = ""
                elif next_button.collidepoint(event.pos) and correct_answer:
                    mystery_city = get_random_city()
                    mystery_country = city_country_mapping[mystery_city]
                    text = ''
                    correct_answer = False
                    incorrect_message = ""
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if is_close(text, mystery_country):
                            correct_answer = True
                            incorrect_message = ""
                        else:
                            incorrect_message = "Incorrect! Try again."

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)

        draw_text(f"Guess the mystery country with the given city: {mystery_city}", font, BLACK, WIDTH // 2, 50)

        width = max(200, font.size(text)[0] + 10)
        input_box.w = width
        pygame.draw.rect(screen, color, input_box, 2)
        draw_text(text, input_font, BLACK, input_box.x + 5, input_box.y + 5)

        draw_button(try_again_button, GREEN, "Try Again", BLACK)
        draw_button(next_button, GREEN if correct_answer else (200, 200, 200), "Next", BLACK)
        draw_button(quit_button, GREEN, "Quit", BLACK)

        draw_text(incorrect_message, font, (255, 0, 0), WIDTH // 2, HEIGHT - 50)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
