function printContent() {
    var printDiv = document.getElementById("print");
    var originalContents = document.body.innerHTML;
    document.body.innerHTML = printDiv.innerHTML;
    window.print();
    document.body.innerHTML = originalContents;
}