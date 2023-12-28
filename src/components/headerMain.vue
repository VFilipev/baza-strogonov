<template lang="pug">
header.p-20    
    .container
        .row.align-items-center.justify-content-between
            .header_logo.col-2.col-sm-5
                router-link(to="/")
                    img(src="../assets/images/logo2.svg")
            ul.header_sticky__nav.col-6.col-sm-3.offset-sm-2.d-flex
                router-link(to="/house" tag="li" class="header_sticky__nav_link") дома                
                router-link(to="/uslugi" tag="li" class="header_sticky__nav_link") активный отдых/услуги
            .header_sticky__icon_feed_back.col-2
                a(href="tel:+79026439294")
                    img(src="../assets/images/telefon2.svg")
                button забронировать
</template>


<style scoped>
.p-20{
    padding: 20px 0px;
}
.header_sticky__nav_link {
    text-decoration: none;
    color: black;
    font-size: 17px;
    font-family: 'Lato';
    font-weight: 300;

    &:after {
        display: block;
        content: '';
        border-bottom: solid 1px black;
        transform: scaleX(0);
        transition: transform 250ms ease-in-out;
    }

    &:hover:after {
        transform: scaleX(1);
    }

}

.header_sticky__nav {
    display: flex;
    gap: 11px;
    font-family: 'Lato';
    font-weight: 300;
    font-size: 17px;
    color: black;
    margin-bottom: 0;
}
.header_sticky__icon_feed_back {
    display: flex;
    justify-content: flex-end;
    padding-right: 20px;
}

.header_sticky__icon_feed_back img {
    margin-right: 8px;
}

.header_sticky__icon_feed_back button {
    background-color: rgba(0, 93, 75, 1);
    color: #fff;
    border: 0px;
    border-radius: 35px;
}
@media (max-width: 1440px){
    .header_logo img{
        width: 68px;
        height: 26px;
    }
    .header_sticky {
    /* width: 100wh; */
    &.active{
        padding-top: 15px;
        padding-bottom: 15px;

    }
}
.header_sticky__nav_link{
    font-size: 10px;
}
.header_sticky__icon_feed_back{
    font-size: 10px;
}
.header_sticky__icon_feed_back a img{
    width: 16px;
}
.header_sticky__icon_feed_back{
    padding-right: calc(var(--bs-gutter-x) * 0.5);
}
}

</style>