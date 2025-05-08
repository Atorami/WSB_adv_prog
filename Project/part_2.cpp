#include <iostream>
#include <vector>
#include <memory>
#include <thread>
#include <chrono>
#include <mutex>

using namespace std;

// 1. Abstrakcyjna klasa bazowa
class WaterVehicle {
protected:
    string name;
    int productionYear;

public:
    WaterVehicle(string n, int year) : name(n), productionYear(year) {}
    virtual void displayInfo() const = 0;
    virtual void unload() = 0;
    virtual void load() = 0;
    virtual ~WaterVehicle() = default;

    // Publiczny getter dla atrybutu name
    string getName() const {
        return name;
    }
};

// 2. Klasy pochodne
class Ship : public WaterVehicle {
    int capacity;

public:
    Ship(string n, int year, int cap) : WaterVehicle(n, year), capacity(cap) {}

    void displayInfo() const override {
        cout << "[Statek] " << name << ", Rok: " << productionYear << ", Ładowność: " << capacity << " ton\n";
    }

    void unload() override {
        cout << "Rozładowywanie statku " << name << "...\n";
    }

    void load() override {
        cout << "Załadowywanie statku " << name << "...\n";
    }
};

class Submarine : public WaterVehicle {
    int maxDepth;

public:
    Submarine(string n, int year, int depth) : WaterVehicle(n, year), maxDepth(depth) {}

    void displayInfo() const override {
        cout << "[Łódź Podwodna] " << name << ", Rok: " << productionYear << ", Maksymalna głębokość zanurzenia: " << maxDepth << " m\n";
    }

    void unload() override {
        cout << "Rozładowywanie łodzi podwodnej " << name << "...\n";
    }

    void load() override {
        cout << "Załadowywanie łodzi podwodnej " << name << "...\n";
    }

    void dive() {
        cout << "Łódź podwodna " << name << " zanurza się!\n";
    }
};

class Sailboat : public WaterVehicle {
    int numberOfSails;

public:
    Sailboat(string n, int year, int sails) : WaterVehicle(n, year), numberOfSails(sails) {}

    void displayInfo() const override {
        cout << "[Żaglowiec] " << name << ", Rok: " << productionYear << ", Liczba żagli: " << numberOfSails << "\n";
    }

    void unload() override {
        cout << "Rozładowywanie żaglowca " << name << "...\n";
    }

    void load() override {
        cout << "Załadowywanie żaglowca " << name << "...\n";
    }

    void raiseSails() {
        cout << "Żaglowiec " << name << " stawia żagle!\n";
    }
};

// 3. Klasa Kapitan
enum class License {
    SHIP,
    SUBMARINE,
    SAILBOAT
};

class Captain {
    string firstName;
    string lastName;
    License license;

public:
    Captain(string first, string last, License lic) : firstName(first), lastName(last), license(lic) {}

    void displayInfo() const {
        cout << "Kapitan: " << firstName << " " << lastName << " | Licencja: ";
        switch (license) {
            case License::SHIP: cout << "Statek"; break;
            case License::SUBMARINE: cout << "Łódź Podwodna"; break;
            case License::SAILBOAT: cout << "Żaglowiec"; break;
        }
        cout << "\n";
    }

    License getLicense() const {
        return license;
    }
};

// 4. Klasa Port
class Port {
    mutex m;
    const chrono::seconds maneuverTime = chrono::seconds(1); // Zmniejszono czas manewru do 1 sekundy

public:
    void acceptVehicle(shared_ptr<WaterVehicle> vehicle) {
        lock_guard<mutex> lock(m);
        cout << ">>> Pojazd " << vehicle->getName() << " wpływa do portu...\n";
        this_thread::sleep_for(maneuverTime);

        vehicle->displayInfo();
        vehicle->unload();
        vehicle->load();

        cout << ">>> Pojazd " << vehicle->getName() << " zacumował w porcie.\n\n";
    }

    void releaseVehicle(shared_ptr<WaterVehicle> vehicle) {
        lock_guard<mutex> lock(m);
        cout << "<<< Pojazd " << vehicle->getName() << " odpływa z portu...\n";
        this_thread::sleep_for(maneuverTime);

        cout << "<<< Pojazd " << vehicle->getName() << " opuścił portu.\n\n";
    }
};

// 5. Użycie polimorfizmu w funkcji demonstracyjnej
int main() {
    Port port;

    auto ship = make_shared<Ship>("Ocean Queen", 2005, 20000);
    auto submarine = make_shared<Submarine>("Deep Explorer", 2012, 800);
    auto sailboat = make_shared<Sailboat>("Wind Rider", 1988, 3);

    Captain shipCaptain("Jan", "Nowak", License::SHIP);
    Captain submarineCaptain("Anna", "Kowalska", License::SUBMARINE);
    Captain sailboatCaptain("Piotr", "Wiatr", License::SAILBOAT);

    shipCaptain.displayInfo();
    port.acceptVehicle(ship);
    port.releaseVehicle(ship);

    submarineCaptain.displayInfo();
    port.acceptVehicle(submarine);
    dynamic_pointer_cast<Submarine>(submarine)->dive();
    port.releaseVehicle(submarine);

    sailboatCaptain.displayInfo();
    port.acceptVehicle(sailboat);
    dynamic_pointer_cast<Sailboat>(sailboat)->raiseSails();
    port.releaseVehicle(sailboat);

    return 0;
}