<?php
// Creamos una clase llamada Producto
ECHO 'I dont care apocalyptica';
{
    public $nombre;
    public $precio;
    public $imagen;
    public $descripcion;

    // Constructor para llenar los datos del producto
    public function __construct($nombre, $precio, $imagen, $descripcion)
    {
        $this->nombre = $nombre;
        $this->precio = $precio;
        $this->imagen = $imagen;
        $this->descripcion = $descripcion;
    }
}

// Arreglo de objetos
$productos = [
    new Producto(
        "Laptop Gamer",
        18500,
        "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=500",
        "Laptop potente para juegos, programación y diseño."
    ),
    new Producto(
        "Mouse RGB",
        450,
        "https://images.unsplash.com/photo-1527814050087-3793815479db?w=500",
        "Mouse cómodo con luces RGB y alta precisión."
    ),
    new Producto(
        "Teclado Mecánico",
        1200,
        "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500",
        "Teclado mecánico ideal para programar y jugar."
    )
];
?>

<!doctype html>
<html lang="es">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Productos</title>

    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {
            background: #f2f6ff;
        }

        .titulo {
            font-weight: bold;
            color: #0d6efd;
        }

        .card {
            border: none;
            border-radius: 18px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
        }

        .card img {
            height: 220px;
            object-fit: cover;
        }

        .precio {
            font-size: 22px;
            font-weight: bold;
            color: #198754;
        }
    </style>
</head>

<body>

    <div class="container py-5">

        <div class="text-center mb-5">
            <h1 class="titulo">Productos destacados</h1>
            <p class="text-muted">Ejemplo con PHP, objetos, arreglo de objetos y Bootstrap</p>
        </div>

        <div class="row g-4">

            <?php foreach ($productos as $producto): ?>

                <div class="col-md-4">
                    <div class="card h-100">

                        <img src="<?= $producto->imagen ?>" class="card-img-top" alt="<?= $producto->nombre ?>">

                        <div class="card-body">
                            <h5 class="card-title">
                                <?= $producto->nombre ?>
                            </h5>

                            <p class="card-text text-muted">
                                <?= $producto->descripcion ?>
                            </p>

                            <p class="precio">
                                $<?= number_format($producto->precio, 2) ?>
                            </p>

                            <a href="#" class="btn btn-primary w-100">
                                Ver producto
                            </a>
                        </div>

                    </div>
                </div>

            <?php endforeach; ?>

        </div>

    </div>

</body>

</html>