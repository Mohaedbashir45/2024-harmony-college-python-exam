# 2024-harmony-college-python-exam
# # Concert Domain Project

This project implements a simple concert domain model using SQLAlchemy ORM. It includes models for Bands, Venues, and Concerts, along with their relationships and various utility methods.

## Author

**Mohamed** Technical Mentor at Harmony College

## Table of Contents

-   [Installation](#installation)
-   [Usage](#usage)
-   [Models](#models)
-   [Configuration](#configuration)
-   [Example](#example)

## Installation

1.  Clone this repository.
2.  Install the required dependencies:
    
    Copy
    
    `pip install sqlalchemy`
    
3.  Set up the database by running the `main.py` script.

## Usage

The main components of this project are:

-   `models.py`: Contains the SQLAlchemy models for Band, Venue, and Concert.
-   `config.py`: Handles database configuration and session management.
-   `main.py`: Provides an example of how to use the models and perform various operations.

To run the example, execute:

Copy

`python main.py`

## Models

### Band

-   Attributes: id, name, hometown
-   Relationships: concerts (one-to-many with Concert)
-   Methods:
    -   `venues()`: List all venues the band has played in
    -   `play_in_venue(venue, date)`: Schedule a new concert
    -   `all_introductions()`: Get introductions for all concerts
    -   `most_performances(db)`: Class method to find the band with most performances

### Venue

-   Attributes: id, title, city
-   Relationships: concerts (one-to-many with Concert)
-   Methods:
    -   `bands()`: List all bands that have played in this venue
    -   `concert_on(date)`: Find a concert on a specific date
    -   `most_frequent_band()`: Find the band that has played most often at this venue

### Concert

-   Attributes: id, date, band_id, venue_id
-   Relationships: band (many-to-one with Band), venue (many-to-one with Venue)
-   Methods:
    -   `hometown_show()`: Check if the concert is in the band's hometown
    -   `introduction()`: Generate an introduction for the concert

## Configuration

The database configuration is set in `config.py`. By default, it uses SQLite with the database file `concert_domain.db`.

## Example

The `main.py` file contains an example that demonstrates how to:

1.  Create bands and venues
2.  Schedule concerts
3.  Query relationships between bands, venues, and concerts
4.  Use various utility methods defined in the models

You can modify this file or create your own scripts to interact with the models as needed for your application.