<template lang="pug"> 
div.container  
  h1.name-section БРОНИРОВАНИЕ 
  section.info 
    .row 
      .col-6.info-form
        div.info-form__text Введите данные:
        input.text-field__input(placeholder="ФИО" type="text")
        input.text-field__input(placeholder="Телефон" type="tel")
        input.text-field__input(placeholder="Email" type="email")
        div.data-time-container
          input.date-time-in
          input.date-time-out
      .col-6.info-card-lodge 
        div Фото
</template>

<script>

export default {
  name: 'booking',
  setup() {
    
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

.name-section {
  font-family: 'Lato';
  font-size: 40px;
  color: rgba(0, 93, 75, 1);
  margin-top: 97px;
  margin-bottom: 47px;
}

.info-form__text {
  font-family: 'Lato';
  font-size: 20px;
  margin-bottom: 21px;
}

.text-field__input {
  border-radius: 9px;
  border: 1px #A4A4A4 solid;
  width: 100%;
  height: 57px;
  padding-left: 10px;
  font-size: 24px;
  font-family: 'Montserrat', sans-serif;
  margin-bottom: 20px;
}

.data-time-container {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.date-time-in {
  width: 275px;
}

.date-time-out {
  width: 275px;
}


</style>
