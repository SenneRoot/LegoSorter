
import java.io.IOException;

import com.hopding.jrpicam.*;
import com.hopding.jrpicam.enums.*;
import com.hopding.jrpicam.exceptions.FailedToRunRaspistillException;

public class test
{
	private static RPiCamera piCamera;
	
	public test()
	{
		
	}
	public static void main(String[] args)
	{
		try {
			piCamera = new RPiCamera("/home/pi/Pictures")
				     .setWidth(500)
				     .setHeight(500)
				     .setBrightness(75)
				     .setExposure(Exposure.AUTO)
				     .setTimeout(2)
				     .setAddRawBayer(true);
		} catch (FailedToRunRaspistillException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
			try {
				piCamera.takeStill("An Awesome Pic.jpg");
			} catch (IOException | InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	}
}