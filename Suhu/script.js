function hitung() {
    const inputForm = document.getElementById("input_form").value;
    const hasilPerhitungan = (parseFloat(inputForm) - 32) * 5 / 9;
    document.getElementById("hasil").innerText = "" + hasilPerhitungan.toFixed(2);
  }