<script type="text/javascript">
    var image_url = '{{ business.image }}'
    var image_url_split = image_url.split("/")

    console.log(image_url_split[5])

    var wrkng_link = 'https://drive.google.com/thumbnail?id=' + image_url_split[5]

    document.getElementById("custom_id").src = wrkng_link
</script>