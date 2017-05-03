import com.hopding.jrpicam.RPiCamera;
import com.hopding.jrpicam.exceptions.FailedToRunRaspistillException;

import org.opencv.core.Mat;
import org.opencv.videoio.VideoCapture;

public class test
{
	private static RPiCamera piCamera;
	
	public test()
	{
		try
		{
			piCamera = new RPiCamera("/home/pi/Snapshots");
		} catch(FailedToRunRaspistillException e) 
		{
			e.printStackTrace();
		}
	}
	public static void main(String[] args)
	{
		piCamera.setSaveDir("/home/pi/AlternativeDirectory");
	}
}