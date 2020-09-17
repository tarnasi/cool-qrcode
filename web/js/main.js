function generate()
{
    $("#loading").removeClass("d-none");
    let textVal = document.getElementById('link').value;

    setTimeout(() => {
        eel.generateQRCode(textVal)(function(res) {
            console.log("Image: ", res);
            $("#loading").addClass("d-none");
            $('#qrcode').removeClass('d-none')
            $("#qrcode-image").attr("src", res)
        })

    }, 1000)
}