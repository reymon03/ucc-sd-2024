import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

public class vehiculos {
    private static final String[] MARCAS = {"Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen"};
    private static final String[] MODELOS = {"Sedán", "SUV", "Hatchback", "Pickup", "Coupé"};
    private static final String[] COLORES = {"Rojo", "Azul", "Blanco", "Negro", "Plateado"};

    private static final Random random = new Random();

    public static void main(String[] args) {
        Timer timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                mostrarInfoVehicular();
            }
        }, 0, 5000); // Ejecutar cada 5000 milisegundos (5 segundos)
    }

    private static void mostrarInfoVehicular() {
        String marca = MARCAS[random.nextInt(MARCAS.length)];
        String modelo = MODELOS[random.nextInt(MODELOS.length)];
        String color = COLORES[random.nextInt(COLORES.length)];
        int año = 2000 + random.nextInt(24); // Años entre 2000 y 2023
        int velocidad = 60 + random.nextInt(141); // Velocidad entre 60 y 200 km/h

        System.out.println("Información Vehicular:");
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Color: " + color);
        System.out.println("Año: " + año);
        System.out.println("Velocidad actual: " + velocidad + " km/h");
        System.out.println("--------------------");
    }
}