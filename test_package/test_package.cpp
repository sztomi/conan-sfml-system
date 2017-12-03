#include <SFML/System.hpp>
#include <iostream>

int main() {
  sf::Clock clock;
  std::cout << "Using SFML v" << SFML_VERSION_MAJOR << "." << SFML_VERSION_MINOR
            << "." << SFML_VERSION_PATCH << "\n";
  std::cout << "Printing that took " << clock.getElapsedTime().asMilliseconds()
            << "ms\n";
  return 0;
}
