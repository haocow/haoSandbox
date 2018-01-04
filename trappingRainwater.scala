object trappingRainwater {
  def trapRain(height: Array[Int]): Int = {
      if (height.length < 2) {
          return 0
      }

      var indL = 0
      var indR = height.length-1

      var currHeight = math.min(height(indL), height(indR))

      var total = 0
      while (indL <= indR) {
          while (indL <= indR && height(indL) <= currHeight) {
            total += (currHeight - height(indL))
            indL += 1
          }

          while (indL <= indR && height(indR) <= currHeight) {
            total += (currHeight - height(indR))
            indR -= 1
          }

          if (indL <= indR) {
              currHeight = math.min(height(indL), height(indR))
          }
      }

      total
  }

  def main(args: Array[String]): Unit = {
      val input = Array(2,0,2)

      val wtf = trapRain(input)
      println(wtf)
  }
}
