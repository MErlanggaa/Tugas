function hitungBMI() {
   // Mengambil nilai berat badan dan tinggi badan dari input
   const beratBadan = parseFloat(document.getElementById("berat_badan").value);
   const tinggiBadanCm = parseFloat(document.getElementById("tinggi_badan").value);

   // Konversi tinggi badan dari cm ke meter
   const tinggiBadanM = tinggiBadanCm / 100;

   // Menghitung BMI
   const bmi = beratBadan / (tinggiBadanM * tinggiBadanM);

   // Menampilkan hasil BMI
   document.getElementById("hasil").innerText = bmi.toFixed(2);

   // Menampilkan status BMI berdasarkan kriteria
   let status = "";
   if (bmi < 18.5) {
       status = "Kurus";
   } else if (bmi >= 18.5 && bmi <= 24.9) {
       status = "Normal";
   } else if (bmi >= 25 && bmi <= 29.9) {
       status = "Overweight";
   } else {
       status = "Obesitas";
   }
   document.getElementById("status").innerText = status;

}