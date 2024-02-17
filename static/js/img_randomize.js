function imgErrorClothe(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/clothing/clothe2.jpg' %}", "{% static 'img/clothing/clothing_placeholder.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorAccessories(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/accessories/accessories.jpg' %}", "{% static 'img/accessories/accessories_2.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorRestaurant(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/restaurants/restaurant_2.jpg' %}", "{% static 'img/restaurants/restaurant_placeholder.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorClub(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/clubs/club_1.jpg' %}", "{% static 'img/clubs/club_2.jpg' %}", "{% static 'img/clubs/club_3.jpg' %}", "{% static 'img/clubs/club_4.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorBeauty(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/beauty/beauty_placeholder.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorCleaning(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/cleaning/cleaning_placeholder.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorProfsrvs(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/professional_services/professional_1.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorConstruction(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/construction/construction_1.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorCoffee(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/coffee/coffee_1.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
    return true;
}

function imgErrorHealth(image) {
    image.onerror = "";
    var imgArray = ["{% static 'img/health_wellness/health_1.jpg' %}"];
    var randomNumber = Math.floor(Math.random()*imgArray.length);
    image.src = imgArray[randomNumber];
}