public class test
{
	public static void main(String[] args)
	{
		RPiCamera piCamera = new RPiCamera("/home/pi/Pictures");
		
		piCamera.setWidth(500).setHeight(500) // Set Camera to produce 500x500 images.
	    .setBrightness(75)                // Adjust Camera's brightness setting.
	    .setExposure(Exposure.AUTO)       // Set Camera's exposure.
	    .setTimeout(2)                    // Set Camera's timeout.
	    .setAddRawBayer(true);            // Add Raw Bayer data to image files created by Camera.
		// Sets all Camera options to their default settings, overriding any changes previously made.
		piCamera.setToDefaults();
		piCamera.takeStill("An Awesome Pic.jpg");
	}
}