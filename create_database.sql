-- Créer la base de données
CREATE DATABASE IF NOT EXISTS hbnb_part2;

-- Utiliser la base de données
USE hbnb_part2;

-- Table User
CREATE TABLE IF NOT EXISTS User (
    id UUID PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table Country
CREATE TABLE IF NOT EXISTS Country (
    id UUID PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    code VARCHAR(10) NOT NULL,
    cities JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table City
CREATE TABLE IF NOT EXISTS City (
    id UUID PRIMARY KEY,
    country_code VARCHAR(10) REFERENCES Country(code),
    name VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table Place
CREATE TABLE IF NOT EXISTS Place (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES User(id),
    city_id UUID REFERENCES City(id),
    name VARCHAR(128) NOT NULL,
    description VARCHAR(255),
    address VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT,
    number_rooms INT DEFAULT 0,
    number_bathrooms INT DEFAULT 0,
    max_guest INT DEFAULT 0,
    price_by_night FLOAT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table Amenity
CREATE TABLE IF NOT EXISTS Amenity (
    id UUID PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table Place_Amenity (Table d'association)
CREATE TABLE IF NOT EXISTS Place_Amenity (
    place_id UUID REFERENCES Place(id),
    amenity_id UUID REFERENCES Amenity(id),
    PRIMARY KEY (place_id, amenity_id)
);

-- Table Review
CREATE TABLE IF NOT EXISTS Review (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES User(id),
    place_id UUID REFERENCES Place(id),
    comment VARCHAR(255) NOT NULL,
    rating FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);