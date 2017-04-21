import java.io.IOException;

import com.hopding.jrpicam.*;
import com.hopding.jrpicam.exceptions.FailedToRunRaspistillException;


public class test
{
	public static void main(String[] args)
	{
		RPiCamera piCamera = null;
		try {
			piCamera = new RPiCamera("/home/pi/Pictures");
		} catch (FailedToRunRaspistillException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		piCamera.setWidth(500).setHeight(500) // Set Camera to produce 500x500 images.
	    .setBrightness(75)                // Adjust Camera's brightness setting.
	    .setExposure(Exposure.AUTO)       // Set Camera's exposure.
	    .setTimeout(2)                    // Set Camera's timeout.
	    .setAddRawBayer(true);            // Add Raw Bayer data to image files created by Camera.
		// Sets all Camera options to their default settings, overriding any changes previously made.
		piCamera.setToDefaults();
		try {
			piCamera.takeStill("An Awesome Pic.jpg");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}