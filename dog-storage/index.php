<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Your notes</title>
  </head>
  <body>
    <h1>Dog Storage</h1>
    <?php
      if ($_GET['id']) {
        $conn = mysqli_connect("localhost", "ctf", "Qwe1234", "ctf");
        $id = mysqli_real_escape_string($conn, $_GET['id']);
        if (strlen($id) > 13) {
          $id = substr($id, strlen($id) - 13, 13);
        }
        $query_raw = "SELECT data FROM notes WHERE id='" . $id . "'";
        $query = mysqli_query($conn, $query_raw) or die("Bad query: " . mysqli_error($conn));
        if (mysqli_num_rows($query) == 0) {
          echo '<p><b>No such article!</b></p>';
        } else {
          echo '<p><b>Here\'s what you\'ve saved:</b></p>';
          while ($row = mysqli_fetch_assoc($query)) {
            echo '<p>', $row['data'], '</p>';
          }
        }
      } else if ($_POST['data']) {
        $conn = mysqli_connect("localhost", "ctf", "Qwe1234", "ctf") or die("Badconnection");
        $data = substr(mysqli_real_escape_string($conn, $_POST['data']), 0, 300);
        $id = uniqid();
        $query = mysqli_query($conn, "INSERT INTO notes (id, data) VALUES ('" . $id . "', '" . $data . "');") or die("Bad query: " . mysqli_error($conn));
        echo "<p><b>Success!</b> Here's your link:</p><p><pre>http://ds.ctf.upml.tech/?id=" . $id . "</pre></p>";
      } else {
    ?>
    <p>You can store your important notices here!</p>
    <p>I'll make unique link for each your note.</p>
    <p>Maximal note length is <b>300 symbols</b>.</p>
    <p>It's very private and secure. Our databases are in safety.</p>
    <form method="post" action="/">
      <textarea name="data" style="width: 100%; min-height: 300px;"></textarea>
      <button>Store</button>
    </form>
    <?php
      }
    ?>
    <hr/>
    <p><small>&copy; Dog Association, 2017</small></p>
  </body>
</html>
